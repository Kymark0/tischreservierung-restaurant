class Table:
    def __init__(self, table_number: int, seats: int, min_people: int = 1) -> None:
        self.table_number = table_number
        self.seats = seats
        self.min_people = min_people
        self.is_active = True

    def can_seat(self, person_count: int) -> bool:
        """Checks if the amount of people can be seated at the table"""
        if self.is_active:
            if person_count < self.min_people or person_count > self.seats:
                return False
            else:
                return True
        return False

    def get_info(self) -> str:
        return (
            f"Tisch {self.table_number}: "
            f"{self.seats} Plätze, "
            f"mindestens {self.min_people} Personen, "
            f"aktiv: {'Ja' if self.is_active else 'Nein'}"
        )

    def activate(self) -> None:
        self.is_active = True

    def deactivate(self) -> None:
        self.is_active = False