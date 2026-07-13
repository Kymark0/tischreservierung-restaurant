from table import Table


class IndoorTable(Table):
    """Represents an indoor table with additional indoor properties."""

    def __init__(
        self,
        table_number: int,
        seats: int,
        min_people: int = 1,
        is_near_window: bool = False,
        is_quiet_area: bool = False,
        has_power_outlet: bool = False,
    ) -> None:
        """Create an indoor table with optional preferences."""
        super().__init__(table_number, seats, min_people)
        self.is_near_window = is_near_window
        self.is_quiet_area = is_quiet_area
        self.has_power_outlet = has_power_outlet

    def get_info(self) -> str:
        """Return the indoor table information as a formatted string."""
        return (
            f"Innentisch {self.table_number}: "
            f"{self.seats} Plätze, "
            f"mindestens {self.min_people} Personen, "
            f"Fensterplatz: {'Ja' if self.is_near_window else 'Nein'}, "
            f"ruhiger Bereich: {'Ja' if self.is_quiet_area else 'Nein'}, "
            f"Steckdose: {'Ja' if self.has_power_outlet else 'Nein'}, "
            f"aktiv: {'Ja' if self.is_active else 'Nein'}"
        )
