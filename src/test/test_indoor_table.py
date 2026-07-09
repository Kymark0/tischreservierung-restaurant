from indoor_table import IndoorTable
from table import Table


def test_indoor_table_is_table() -> None:
    table = IndoorTable(table_number=1, seats=4)

    assert isinstance(table, Table)


def test_indoor_table_stores_indoor_attributes() -> None:
    table = IndoorTable(
        table_number=1,
        seats=4,
        min_people=2,
        is_near_window=True,
        is_quiet_area=True,
        has_power_outlet=True
    )

    assert table.table_number == 1
    assert table.seats == 4
    assert table.min_people == 2
    assert table.is_near_window is True
    assert table.is_quiet_area is True
    assert table.has_power_outlet is True