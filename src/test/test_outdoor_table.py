from outdoor_table import OutdoorTable
from table import Table


def test_outdoor_table_is_table() -> None:
    table = OutdoorTable(table_number=2, seats=6)

    assert isinstance(table, Table)


def test_outdoor_table_stores_outdoor_attributes() -> None:
    table = OutdoorTable(
        table_number=2,
        seats=6,
        min_people=2,
        has_heater=True,
        is_rainproof=True,
        is_windproof=True,
        allows_smoking=False,
    )

    assert table.table_number == 2
    assert table.seats == 6
    assert table.min_people == 2
    assert table.has_heater is True
    assert table.is_rainproof is True
    assert table.is_windproof is True
    assert table.allows_smoking is False
