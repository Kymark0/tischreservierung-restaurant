from datetime import date as Date
from datetime import time as Time

from customer import Customer


class Reservation:
    def __init__(
        self,
        reservation_id: int,
        customer: Customer,
        date: Date,
        time: Time,
        person_count: int,
        table_number: int,
        status: str = "aktiv"
    ) -> None:
        self.reservation_id = reservation_id
        self.customer = customer
        self.date = date
        self.time = time
        self.person_count = person_count
        self.table_number = table_number
        self.status = status

    def cancel(self) -> None:
        # TODO: Status der Reservierung auf storniert setzen.
        pass

    def is_active(self) -> bool:
        # TODO: Prüfen, ob die Reservierung aktiv ist.
        pass

    def get_info(self) -> str:
        # TODO: Reservierungsdaten formatiert zurückgeben.
        pass