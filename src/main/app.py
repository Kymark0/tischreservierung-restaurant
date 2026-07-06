import streamlit as st

from customer import Customer
from indoor_table import IndoorTable
from outdoor_table import OutdoorTable
from reservation_system import ReservationSystem


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

    if len(reservation_system.tables) == 0:
        st.warning(
            "Es wurden noch keine Tische angelegt. "
            "Bitte lege zuerst mindestens einen Tisch an."
        )
    else:
        st.subheader("Kundendaten")

        customer_name = st.text_input("Name des Kunden")
        phone_number = st.text_input("Telefonnummer")
        email = st.text_input("E-Mail-Adresse optional")

        st.subheader("Reservierungsdaten")

        reservation_date = st.date_input("Datum")
        reservation_time = st.time_input("Uhrzeit")

        person_count = st.number_input(
            "Personenzahl",
            min_value=1,
            step=1
        )

        st.subheader("Tischwünsche")

        preferred_area = st.selectbox(
            "Gewünschter Bereich",
            ["Egal", "Innen", "Außen"]
        )

        wants_window = False
        wants_quiet_area = False
        wants_power_outlet = False

        wants_heater = False
        wants_rainproof = False
        wants_windproof = False
        smoking_preference = "Egal"

        if preferred_area == "Innen":
            wants_window = st.checkbox("Fensterplatz gewünscht")
            wants_quiet_area = st.checkbox("Ruhiger Bereich gewünscht")
            wants_power_outlet = st.checkbox("Steckdose gewünscht")

        elif preferred_area == "Außen":
            wants_heater = st.checkbox("Heizstrahler gewünscht")
            wants_rainproof = st.checkbox("Regengeschützter Tisch gewünscht")
            wants_windproof = st.checkbox("Windgeschützter Tisch gewünscht")

            smoking_preference = st.selectbox(
                "Raucherbereich",
                ["Egal", "Raucherbereich", "Nichtraucherbereich"]
            )

        if st.button("Reservierung erstellen"):
            if customer_name.strip() == "":
                st.error("Bitte gib einen Kundennamen ein.")
            elif phone_number.strip() == "":
                st.error("Bitte gib eine Telefonnummer ein.")
            else:
                customer = Customer(
                    name=customer_name,
                    phone_number=phone_number,
                    email=email
                )

                reservation = reservation_system.create_reservation(
                    customer=customer,
                    date=reservation_date,
                    time=reservation_time,
                    person_count=person_count,
                    preferred_area=preferred_area,
                    wants_window=wants_window,
                    wants_quiet_area=wants_quiet_area,
                    wants_power_outlet=wants_power_outlet,
                    wants_heater=wants_heater,
                    wants_rainproof=wants_rainproof,
                    wants_windproof=wants_windproof,
                    smoking_preference=smoking_preference
                )

                if reservation is None:
                    st.error("Es wurde kein passender freier Tisch gefunden.")
                else:
                    st.success(
                        f"Reservierung wurde erstellt. "
                        f"Zugewiesener Tisch: {reservation.table_number}"
                    )


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