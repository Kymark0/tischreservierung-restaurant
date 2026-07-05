class Table:
    def __init__(self, table_number: int, seats: int, min_people: int = 1) -> None:
        self.table_number = table_number
        self.seats = seats
        self.min_people = min_people
        self.is_active = True

    def can_seat(self, person_count: int) -> bool:
        # TODO: Prüfen, ob die Personenzahl zwischen min_people und seats liegt.
        pass

    def get_info(self) -> str:
        # TODO: Allgemeine Tischinformationen zurückgeben.
        pass

    def activate(self) -> None:
        # TODO: Tisch wieder für Reservierungen aktivieren.
        pass

    def deactivate(self) -> None:
        # TODO: Tisch für Reservierungen sperren.
        pass