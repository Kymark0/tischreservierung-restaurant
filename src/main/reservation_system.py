from datetime import date as Date
from datetime import time as Time

from customer import Customer
from reservation import Reservation
from table import Table


class ReservationSystem:
    def __init__(self) -> None:
        self.tables: list[Table] = []
        self.reservations: list[Reservation] = []
        self.next_reservation_id = 1

    def add_table(self, table: Table) -> None:
        # TODO: Tisch zur Tischliste hinzufügen.
        pass

    def is_table_available(
        self,
        table_number: int,
        date: Date,
        time: Time
    ) -> bool:
        # TODO: Prüfen, ob der Tisch zu Datum und Uhrzeit frei ist.
        pass

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
        # TODO: Freien Tisch suchen, der Personenzahl, Zeitpunkt und Wünsche erfüllt.
        pass

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
        # TODO: Reservierung erstellen, wenn ein passender Tisch gefunden wurde.
        pass

    def cancel_reservation(self, reservation_id: int) -> bool:
        # TODO: Reservierung anhand der ID suchen und stornieren.
        pass

    def get_active_reservations(self) -> list[Reservation]:
        # TODO: Alle aktiven Reservierungen zurückgeben.
        pass