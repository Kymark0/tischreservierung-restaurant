class Table:
    """Represents a general restaurant table."""

    def __init__(
        self,
        table_number: int,
        seats: int,
        min_people: int = 1
    ) -> None:
        """Create a table with number, seats and minimum people."""
        self.table_number = table_number
        self.seats = seats
        self.min_people = min_people
        self.is_active = True

    def can_seat(self, person_count: int) -> bool:
        """Return True if the table can seat the given number of people."""
        if not self.is_active:
            return False

        if person_count < self.min_people:
            return False

        if person_count > self.seats:
            return False

        return True

    def get_info(self) -> str:
        """Return the table information as a formatted string."""
        return (
            f"Tisch {self.table_number}: "
            f"{self.seats} Plätze, "
            f"mindestens {self.min_people} Personen, "
            f"aktiv: {'Ja' if self.is_active else 'Nein'}"
        )

    def activate(self) -> None:
        """Set the table status to active."""
        self.is_active = True

    def deactivate(self) -> None:
        """Set the table status to inactive."""
        self.is_active = False