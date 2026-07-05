import streamlit as st

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

    st.write(
        "Hier können später Innen- und Außentische angelegt und angezeigt werden."
    )

    st.subheader("Tisch hinzufügen")

    st.info("TODO: Formular zum Hinzufügen von IndoorTable und OutdoorTable ergänzen.")

    st.subheader("Vorhandene Tische")

    if len(reservation_system.tables) == 0:
        st.warning("Es wurden noch keine Tische angelegt.")
    else:
        for table in reservation_system.tables:
            st.write(table.get_info())


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