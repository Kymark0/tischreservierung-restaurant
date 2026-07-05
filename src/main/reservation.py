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
        self.status = "storneirt"

    def is_active(self) -> bool:
        if self.status == "aktiv":
            return True
        return False

    def get_info(self) -> str:
        return (
            f"Reservierung {self.reservation_id}: "
            f"{self.customer.name}, "
            f"{self.person_count} Personen, "
            f"Datum: {self.date.strftime('%d.%m.%Y')}, "
            f"Uhrzeit: {self.time.strftime('%H:%M')}, "
            f"Tisch: {self.table_number}, "
            f"Status: {self.status}"
        )