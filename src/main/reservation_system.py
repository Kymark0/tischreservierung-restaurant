from datetime import date as Date
from datetime import time as Time

from customer import Customer
from reservation import Reservation
from table import Table
from indoor_table import IndoorTable
from outdoor_table import OutdoorTable


class ReservationSystem:
    def __init__(self) -> None:
        self.tables: list[Table] = []
        self.reservations: list[Reservation] = []
        self.next_reservation_id = 1

    def add_table(self, table: Table) -> bool:
        for existing_table in self.tables:
            if existing_table.table_number == table.table_number:
                return False

        self.tables.append(table)
        return True
    
    def remove_table(self, table_number: int) -> bool:
        for table in self.tables:
            if table.table_number == table_number:
                self.tables.remove(table)
                return True

        return False
    
    def is_table_available(
        self,
        table_number: int,
        date: Date,
        time: Time
    ) -> bool:
        for reservation in self.reservations:
            if (
                reservation.table_number == table_number
                and reservation.date == date
                and reservation.time == time
                and reservation.is_active()
            ):
                return False

        return True

    def find_available_table(
        self,
        date: Date,
        time: Time,
        person_count: int,
        preferred_area: str = "Egal",
        wants_window: bool = False,
        wants_quiet_area: bool = False,
        wants_power_outlet: bool = False,
        wants_heater: bool = False,
        wants_rainproof: bool = False,
        wants_windproof: bool = False,
        smoking_preference: str = "Egal"
    ) -> Table | None:
        for table in self.tables:
            if not table.can_seat(person_count):
                continue

            if not self.is_table_available(table.table_number, date, time):
                continue

            if preferred_area == "Innen" and not isinstance(table, IndoorTable):
                continue

            if preferred_area == "Außen" and not isinstance(table, OutdoorTable):
                continue

            if isinstance(table, IndoorTable):
                if wants_window and not table.is_near_window:
                    continue

                if wants_quiet_area and not table.is_quiet_area:
                    continue

                if wants_power_outlet and not table.has_power_outlet:
                    continue

            if isinstance(table, OutdoorTable):
                if wants_heater and not table.has_heater:
                    continue

                if wants_rainproof and not table.is_rainproof:
                    continue

                if wants_windproof and not table.is_windproof:
                    continue

                if (
                    smoking_preference == "Raucherbereich"
                    and not table.allows_smoking
                ):
                    continue

                if (
                    smoking_preference == "Nichtraucherbereich"
                    and table.allows_smoking
                ):
                    continue

            if (
                (wants_window or wants_quiet_area or wants_power_outlet)
                and not isinstance(table, IndoorTable)
            ):
                continue

            if (
                (wants_heater or wants_rainproof or wants_windproof)
                and not isinstance(table, OutdoorTable)
            ):
                continue

            if (
                smoking_preference != "Egal"
                and not isinstance(table, OutdoorTable)
            ):
                continue

            return table

        return None


    def create_reservation(
        self,
        customer: Customer,
        date: Date,
        time: Time,
        person_count: int,
        preferred_area: str = "Egal",
        wants_window: bool = False,
        wants_quiet_area: bool = False,
        wants_power_outlet: bool = False,
        wants_heater: bool = False,
        wants_rainproof: bool = False,
        wants_windproof: bool = False,
        smoking_preference: str = "Egal"
    ) -> Reservation | None:
        table = self.find_available_table(
            date,
            time,
            person_count,
            preferred_area,
            wants_window,
            wants_quiet_area,
            wants_power_outlet,
            wants_heater,
            wants_rainproof,
            wants_windproof,
            smoking_preference
        )

        if table is None:
            return None

        reservation = Reservation(
            self.next_reservation_id,
            customer,
            date,
            time,
            person_count,
            table.table_number
        )

        self.reservations.append(reservation)
        self.next_reservation_id += 1

        return reservation

    def cancel_reservation(self, reservation_id: int) -> bool:
        for reservation in self.reservations:
            if reservation.reservation_id == reservation_id:
                reservation.cancel()
                return True

        return False

    def get_active_reservations(self) -> list[Reservation]:
        active_reservations = []

        for reservation in self.reservations:
            if reservation.is_active():
                active_reservations.append(reservation)

        return active_reservations