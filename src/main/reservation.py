from datetime import date as Date
from datetime import time as Time

from customer import Customer


class Reservation:
    """Represents a restaurant reservation for one customer and table."""

    def __init__(
        self,
        reservation_id: int,
        customer: Customer,
        date: Date,
        time: Time,
        person_count: int,
        table_number: int,
        duration_hours: int = 1,
        status: str = "aktiv",
    ) -> None:
        """Create a reservation with customer, time and table data."""
        self.reservation_id = reservation_id
        self.customer = customer
        self.date = date
        self.time = time
        self.person_count = person_count
        self.table_number = table_number
        self.duration_hours = duration_hours
        self.status = status

    def cancel(self) -> None:
        """Cancel the reservation by changing its status."""
        self.status = "storniert"

    def is_active(self) -> bool:
        """Return True if the reservation is active."""
        if self.status == "aktiv":
            return True

        return False

    def get_info(self) -> str:
        """Return the reservation information as a formatted string."""
        return (
            f"Reservierung {self.reservation_id}: "
            f"{self.customer.name}, "
            f"{self.person_count} Personen, "
            f"Datum: {self.date.strftime('%d.%m.%Y')}, "
            f"Uhrzeit: {self.time.strftime('%H:%M')}, "
            f"Dauer: {self.duration_hours} Stunde(n), "
            f"Tisch: {self.table_number}, "
            f"Status: {self.status}"
        )
