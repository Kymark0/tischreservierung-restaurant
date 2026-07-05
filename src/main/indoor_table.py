from table import Table


class IndoorTable(Table):
    def __init__(
        self,
        table_number: int,
        seats: int,
        min_people: int = 1,
        is_near_window: bool = False,
        is_quiet_area: bool = False,
        has_power_outlet: bool = False
    ) -> None:
        super().__init__(table_number, seats, min_people)
        self.is_near_window = is_near_window
        self.is_quiet_area = is_quiet_area
        self.has_power_outlet = has_power_outlet

    def get_info(self) -> str:
        # TODO: Informationen zum Innentisch zurückgeben.
        pass