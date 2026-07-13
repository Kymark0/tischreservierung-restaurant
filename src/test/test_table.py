from table import Table


def test_table_stores_attributes() -> None:
    table = Table(table_number=1, seats=4, min_people=2)

    assert table.table_number == 1
    assert table.seats == 4
    assert table.min_people == 2
    assert table.is_active is True


def test_can_seat_returns_true_for_valid_person_count() -> None:
    table = Table(table_number=1, seats=4, min_people=2)

    assert table.can_seat(3) is True


def test_can_seat_returns_false_for_too_few_people() -> None:
    table = Table(table_number=1, seats=4, min_people=2)

    assert table.can_seat(1) is False


def test_can_seat_returns_false_for_too_many_people() -> None:
    table = Table(table_number=1, seats=4, min_people=2)

    assert table.can_seat(5) is False


def test_deactivate_blocks_table_for_reservations() -> None:
    table = Table(table_number=1, seats=4)

    table.deactivate()

    assert table.is_active is False
    assert table.can_seat(2) is False


def test_activate_makes_table_available_again() -> None:
    table = Table(table_number=1, seats=4)
    table.deactivate()

    table.activate()

    assert table.is_active is True
    assert table.can_seat(2) is True
