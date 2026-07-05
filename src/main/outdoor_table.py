from table import Table


class OutdoorTable(Table):
    def __init__(
        self,
        table_number: int,
        seats: int,
        min_people: int = 1,
        has_heater: bool = False,
        is_rainproof: bool = False,
        is_windproof: bool = False,
        allows_smoking: bool = False
    ) -> None:
        super().__init__(table_number, seats, min_people)
        self.has_heater = has_heater
        self.is_rainproof = is_rainproof
        self.is_windproof = is_windproof
        self.allows_smoking = allows_smoking

    def get_info(self) -> str:
        # TODO: Informationen zum Außentisch zurückgeben.
        pass