import streamlit as st

from reservation_system import ReservationSystem
from indoor_table import IndoorTable
from outdoor_table import OutdoorTable

st.set_page_config(
    page_title="Restaurant-Tischreservierung",
    layout="wide"
)

st.title("Restaurant-Tischreservierung")

if "reservation_system" not in st.session_state:
    st.session_state.reservation_system = ReservationSystem()

reservation_system = st.session_state.reservation_system

tab_tables, tab_create_reservation, tab_show_reservations, tab_cancel = st.tabs(
    [
        "Tische verwalten",
        "Reservierung erstellen",
        "Reservierungen anzeigen",
        "Reservierung stornieren"
    ]
)

with tab_tables:
    st.header("Tische verwalten")

    st.subheader("Tisch hinzufügen")

    table_type = st.selectbox(
        "Tischart auswählen",
        ["Innentisch", "Außentisch"]
    )

    table_number = st.number_input(
        "Tischnummer",
        min_value=1,
        step=1
    )

    seats = st.number_input(
        "Sitzplätze",
        min_value=1,
        step=1
    )

    min_people = st.number_input(
        "Mindestanzahl Personen",
        min_value=1,
        max_value=seats,
        step=1
    )

    if table_type == "Innentisch":
        is_near_window = st.checkbox("Fensterplatz")
        is_quiet_area = st.checkbox("Ruhiger Bereich")
        has_power_outlet = st.checkbox("Steckdose vorhanden")

        if st.button("Innentisch hinzufügen"):
            table = IndoorTable(
                table_number=table_number,
                seats=seats,
                min_people=min_people,
                is_near_window=is_near_window,
                is_quiet_area=is_quiet_area,
                has_power_outlet=has_power_outlet
            )

            reservation_system.add_table(table)

            st.success("Innentisch wurde hinzugefügt.")

    else:
        has_heater = st.checkbox("Heizstrahler vorhanden")
        is_rainproof = st.checkbox("Regengeschützt")
        is_windproof = st.checkbox("Windgeschützt")
        allows_smoking = st.checkbox("Raucherbereich")

        if st.button("Außentisch hinzufügen"):
            table = OutdoorTable(
                table_number=table_number,
                seats=seats,
                min_people=min_people,
                has_heater=has_heater,
                is_rainproof=is_rainproof,
                is_windproof=is_windproof,
                allows_smoking=allows_smoking
            )

            reservation_system.add_table(table)

            st.success("Außentisch wurde hinzugefügt.")

    st.subheader("Vorhandene Tische")

    if len(reservation_system.tables) == 0:
        st.warning("Es wurden noch keine Tische angelegt.")
    else:
        table_data = []

        for table in reservation_system.tables:
            table_data.append(
                {
                    "Tischnummer": table.table_number,
                    "Sitzplätze": table.seats,
                    "Mindestpersonen": table.min_people,
                    "Aktiv": "Ja" if table.is_active else "Nein",
                    "Informationen": table.get_info()
                }
            )

        st.table(table_data)


with tab_create_reservation:
    st.header("Reservierung erstellen")

    st.write(
        "Hier kann später eine Reservierung mit Kundendaten, Datum, Uhrzeit, "
        "Personenzahl und Tischwünschen erstellt werden."
    )

    st.info("TODO: Formular zum Erstellen einer Reservierung ergänzen.")


with tab_show_reservations:
    st.header("Reservierungen anzeigen")

    st.write("Hier werden später alle Reservierungen angezeigt.")

    if len(reservation_system.reservations) == 0:
        st.warning("Es wurden noch keine Reservierungen erstellt.")
    else:
        for reservation in reservation_system.reservations:
            st.write(reservation.get_info())


with tab_cancel:
    st.header("Reservierung stornieren")

    st.write(
        "Hier kann später eine Reservierung über ihre Reservierungs-ID storniert werden."
    )

    st.info("TODO: Formular zum Stornieren einer Reservierung ergänzen.")