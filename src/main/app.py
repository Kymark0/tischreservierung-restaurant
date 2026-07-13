"""Streamlit user interface for the restaurant reservation system."""

import streamlit as st
import re

from customer import Customer
from indoor_table import IndoorTable
from outdoor_table import OutdoorTable
from reservation_system import ReservationSystem


def is_valid_email(email: str) -> bool:
    """Return True if the given email has a valid basic format."""
    email_pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(email_pattern, email) is not None


st.set_page_config(page_title="Restaurant-Tischreservierung", layout="wide")

st.title("Restaurant-Tischreservierung")

if "success_message" in st.session_state:
    st.success(st.session_state.success_message)
    del st.session_state.success_message

if "reservation_system" not in st.session_state:
    st.session_state.reservation_system = ReservationSystem()

reservation_system = st.session_state.reservation_system

tab_tables, tab_create_reservation, tab_show_reservations, tab_cancel = (
    st.tabs(
        [
            "Tische verwalten",
            "Reservierung erstellen",
            "Reservierungen anzeigen",
            "Reservierung stornieren",
        ],
        key="active_tab",
        on_change="rerun",
    )
)


with tab_tables:
    st.header("Tische verwalten")

    # Input area for creating new tables.
    st.subheader("Tisch hinzufügen")

    table_type = st.selectbox(
        "Tischart auswählen", ["Innentisch", "Außentisch"]
    )

    table_number = st.number_input("Tischnummer", min_value=1, step=1)

    seats = st.number_input("Sitzplätze", min_value=1, step=1)

    min_people = st.number_input(
        "Mindestanzahl Personen", min_value=1, max_value=seats, step=1
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
                has_power_outlet=has_power_outlet,
            )

            success = reservation_system.add_table(table)

            if success:
                st.success("Innentisch wurde hinzugefügt.")
            else:
                st.error(
                    "Es existiert bereits ein Tisch mit dieser " "Tischnummer."
                )

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
                allows_smoking=allows_smoking,
            )

            success = reservation_system.add_table(table)

            if success:
                st.success("Außentisch wurde hinzugefügt.")
            else:
                st.error(
                    "Es existiert bereits ein Tisch mit dieser " "Tischnummer."
                )

    # Overview and management area for existing tables.
    st.subheader("Vorhandene Tische")

    if len(reservation_system.tables) == 0:
        st.warning("Es wurden noch keine Tische angelegt.")
    else:
        for table in reservation_system.tables:
            col_info, col_status, col_delete = st.columns([4, 1, 1])

            with col_info:
                st.write(f"**Tisch {table.table_number}**")
                st.write(
                    f"Sitzplätze: {table.seats} | "
                    f"Mindestpersonen: {table.min_people} | "
                    f"Aktiv: {'Ja' if table.is_active else 'Nein'}"
                )
                st.caption(table.get_info())

            with col_status:
                if table.is_active:
                    if st.button(
                        "Deaktivieren",
                        key=f"deactivate_table_{table.table_number}",
                    ):
                        if reservation_system.has_reservations_for_table(
                            table.table_number
                        ):
                            st.error(
                                "Dieser Tisch kann nicht deaktiviert werden, "
                                "weil dafür aktive Reservierungen existieren."
                            )
                        else:
                            success = reservation_system.deactivate_table(
                                table.table_number
                            )

                            if success:
                                st.session_state.success_message = (
                                    "Tisch wurde deaktiviert."
                                )
                                st.rerun()
                            else:
                                st.error("Tisch wurde nicht gefunden.")
                else:
                    if st.button(
                        "Aktivieren",
                        key=f"activate_table_{table.table_number}",
                    ):
                        success = reservation_system.activate_table(
                            table.table_number
                        )

                        if success:
                            st.session_state.success_message = (
                                "Tisch wurde aktiviert."
                            )
                            st.rerun()
                        else:
                            st.error("Tisch wurde nicht gefunden.")

            with col_delete:
                if st.button(
                    "Löschen", key=f"delete_table_{table.table_number}"
                ):
                    if reservation_system.has_reservations_for_table(
                        table.table_number
                    ):
                        st.error(
                            "Dieser Tisch kann nicht gelöscht werden, "
                            "weil dafür Reservierungen existieren."
                        )
                    else:
                        success = reservation_system.remove_table(
                            table.table_number
                        )

                        if success:
                            st.session_state.success_message = (
                                "Tisch wurde gelöscht."
                            )
                            st.rerun()
                        else:
                            st.error("Tisch wurde nicht gefunden.")

            st.divider()


with tab_create_reservation:
    st.header("Reservierung erstellen")

    if len(reservation_system.tables) == 0:
        st.warning(
            "Es wurden noch keine Tische angelegt. "
            "Bitte lege zuerst mindestens einen Tisch an."
        )
    else:
        # Customer input fields.
        st.subheader("Kundendaten")

        customer_name = st.text_input("Name des Kunden")
        phone_number = st.text_input("Telefonnummer")
        email = st.text_input("E-Mail-Adresse optional")

        # Reservation input fields.
        st.subheader("Reservierungsdaten")

        reservation_date = st.date_input("Datum")
        reservation_time = st.time_input("Uhrzeit")

        duration_hours = st.number_input(
            "Dauer in Stunden", min_value=1, step=1
        )

        person_count = st.number_input("Personenzahl", min_value=1, step=1)

        # Optional table preferences.
        st.subheader("Tischwünsche")

        preferred_area = st.selectbox(
            "Gewünschter Bereich", ["Egal", "Innen", "Außen"]
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
                ["Egal", "Raucherbereich", "Nichtraucherbereich"],
            )

        if st.button("Reservierung erstellen"):
            customer_name = customer_name.strip()
            phone_number = phone_number.strip()
            email = email.strip()

            if customer_name == "":
                st.error("Bitte gib einen Kundennamen ein.")

            elif phone_number == "":
                st.error("Bitte gib eine Telefonnummer ein.")

            elif not phone_number.isdigit():
                st.error("Die Telefonnummer darf nur Zahlen enthalten.")

            elif email != "" and not is_valid_email(email):
                st.error("Bitte gib eine gültige E-Mail-Adresse ein.")

            else:
                customer = Customer(
                    name=customer_name, phone_number=phone_number, email=email
                )

                reservation = reservation_system.create_reservation(
                    customer=customer,
                    date=reservation_date,
                    time=reservation_time,
                    person_count=person_count,
                    duration_hours=duration_hours,
                    preferred_area=preferred_area,
                    wants_window=wants_window,
                    wants_quiet_area=wants_quiet_area,
                    wants_power_outlet=wants_power_outlet,
                    wants_heater=wants_heater,
                    wants_rainproof=wants_rainproof,
                    wants_windproof=wants_windproof,
                    smoking_preference=smoking_preference,
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

    if len(reservation_system.reservations) == 0:
        st.warning("Es wurden noch keine Reservierungen erstellt.")
    else:
        reservation_data = []

        for reservation in reservation_system.reservations:
            reservation_data.append(
                {
                    "Reservierungs-ID": reservation.reservation_id,
                    "Kunde": reservation.customer.name,
                    "Telefonnummer": reservation.customer.phone_number,
                    "E-Mail": reservation.customer.email,
                    "Datum": reservation.date.strftime("%d.%m.%Y"),
                    "Uhrzeit": reservation.time.strftime("%H:%M"),
                    "Dauer": f"{reservation.duration_hours} Stunde(n)",
                    "Personen": reservation.person_count,
                    "Tisch": reservation.table_number,
                    "Status": reservation.status,
                }
            )

        st.table(reservation_data)


with tab_cancel:
    st.header("Reservierung stornieren")

    active_reservations = reservation_system.get_active_reservations()

    if len(active_reservations) == 0:
        st.warning("Es gibt keine aktiven Reservierungen zum Stornieren.")
    else:
        reservation_options = {}

        for reservation in active_reservations:
            label = (
                f"ID {reservation.reservation_id} | "
                f"{reservation.customer.name} | "
                f"{reservation.date.strftime('%d.%m.%Y')} | "
                f"{reservation.time.strftime('%H:%M')} | "
                f"{reservation.duration_hours} Stunde(n) | "
                f"Tisch {reservation.table_number}"
            )

            reservation_options[label] = reservation.reservation_id

        selected_reservation = st.selectbox(
            "Reservierung auswählen", list(reservation_options.keys())
        )

        if st.button("Reservierung stornieren"):
            reservation_id = reservation_options[selected_reservation]

            success = reservation_system.cancel_reservation(reservation_id)

            if success:
                st.success("Reservierung wurde storniert.")
            else:
                st.error("Reservierung wurde nicht gefunden.")
