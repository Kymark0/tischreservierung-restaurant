from datetime import date as Date
from datetime import time as Time

from customer import Customer
from indoor_table import IndoorTable
from outdoor_table import OutdoorTable
from reservation_system import ReservationSystem


def test_reservation_system_starts_empty() -> None:
    system = ReservationSystem()

    assert system.tables == []
    assert system.reservations == []
    assert system.next_reservation_id == 1


def test_add_table_adds_table_to_list() -> None:
    system = ReservationSystem()
    table = IndoorTable(table_number=1, seats=4)

    system.add_table(table)

    assert len(system.tables) == 1
    assert system.tables[0] == table


def test_is_table_available_returns_true_if_no_reservation_exists() -> None:
    system = ReservationSystem()

    result = system.is_table_available(
        table_number=1, date=Date(2026, 7, 10), time=Time(18, 0)
    )

    assert result is True


def test_create_reservation_adds_reservation() -> None:
    system = ReservationSystem()
    table = IndoorTable(table_number=1, seats=4)
    customer = Customer("Max Mustermann", "0123456789")

    system.add_table(table)

    reservation = system.create_reservation(
        customer=customer,
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=2,
    )

    assert reservation is not None
    assert reservation.reservation_id == 1
    assert reservation.table_number == 1
    assert len(system.reservations) == 1
    assert system.next_reservation_id == 2


def test_is_table_available_returns_false_if_active_reservation_exists() -> (
    None
):
    system = ReservationSystem()
    table = IndoorTable(table_number=1, seats=4)
    customer = Customer("Max Mustermann", "0123456789")

    system.add_table(table)

    system.create_reservation(
        customer=customer,
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=2,
    )

    result = system.is_table_available(
        table_number=1, date=Date(2026, 7, 10), time=Time(18, 0)
    )

    assert result is False


def test_create_reservation_returns_none_if_no_table_is_available() -> None:
    system = ReservationSystem()
    table = IndoorTable(table_number=1, seats=2)
    customer = Customer("Max Mustermann", "0123456789")

    system.add_table(table)

    reservation = system.create_reservation(
        customer=customer,
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=5,
    )

    assert reservation is None


def test_cancel_reservation_changes_status() -> None:
    system = ReservationSystem()
    table = IndoorTable(table_number=1, seats=4)
    customer = Customer("Max Mustermann", "0123456789")

    system.add_table(table)

    reservation = system.create_reservation(
        customer=customer,
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=2,
    )

    assert reservation is not None

    success = system.cancel_reservation(reservation.reservation_id)

    assert success is True
    assert reservation.status == "storniert"


def test_get_active_reservations_only_returns_active_reservations() -> None:
    system = ReservationSystem()
    table_1 = IndoorTable(table_number=1, seats=4)
    table_2 = IndoorTable(table_number=2, seats=4)
    customer = Customer("Max Mustermann", "0123456789")

    system.add_table(table_1)
    system.add_table(table_2)

    reservation_1 = system.create_reservation(
        customer=customer,
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=2,
    )

    reservation_2 = system.create_reservation(
        customer=customer,
        date=Date(2026, 7, 10),
        time=Time(19, 0),
        person_count=2,
    )

    assert reservation_1 is not None
    assert reservation_2 is not None

    reservation_1.cancel()

    active_reservations = system.get_active_reservations()

    assert reservation_1 not in active_reservations
    assert reservation_2 in active_reservations


def test_find_available_table_filters_indoor_preferences() -> None:
    system = ReservationSystem()

    wrong_table = IndoorTable(
        table_number=1,
        seats=4,
        is_near_window=False,
        is_quiet_area=False,
        has_power_outlet=False,
    )

    matching_table = IndoorTable(
        table_number=2,
        seats=4,
        is_near_window=True,
        is_quiet_area=True,
        has_power_outlet=True,
    )

    system.add_table(wrong_table)
    system.add_table(matching_table)

    table = system.find_available_table(
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=2,
        preferred_area="Innen",
        wants_window=True,
        wants_quiet_area=True,
        wants_power_outlet=True,
    )

    assert table == matching_table


def test_find_available_table_filters_outdoor_preferences() -> None:
    system = ReservationSystem()

    wrong_table = OutdoorTable(
        table_number=1,
        seats=4,
        has_heater=False,
        is_rainproof=False,
        is_windproof=False,
        allows_smoking=False,
    )

    matching_table = OutdoorTable(
        table_number=2,
        seats=4,
        has_heater=True,
        is_rainproof=True,
        is_windproof=True,
        allows_smoking=True,
    )

    system.add_table(wrong_table)
    system.add_table(matching_table)

    table = system.find_available_table(
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=2,
        preferred_area="Außen",
        wants_heater=True,
        wants_rainproof=True,
        wants_windproof=True,
        smoking_preference="Raucherbereich",
    )

    assert table == matching_table


def test_find_available_table_with_some_but_not_all_preferences() -> None:
    system = ReservationSystem()

    table_with_power_outlet = IndoorTable(
        table_number=1,
        seats=4,
        is_near_window=True,
        is_quiet_area=False,
        has_power_outlet=True,
    )

    system.add_table(table_with_power_outlet)

    table = system.find_available_table(
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=2,
        preferred_area="Innen",
        wants_window=True,
        wants_power_outlet=True,
    )

    assert table == table_with_power_outlet


def test_add_table_rejects_duplicate_table_number() -> None:
    system = ReservationSystem()

    first_table = IndoorTable(table_number=1, seats=4, min_people=1)
    second_table = IndoorTable(table_number=1, seats=6, min_people=1)

    first_result = system.add_table(first_table)
    second_result = system.add_table(second_table)

    assert first_result is True
    assert second_result is False
    assert len(system.tables) == 1
    assert system.tables[0] == first_table


def test_remove_table_removes_existing_table() -> None:
    system = ReservationSystem()
    table = IndoorTable(table_number=1, seats=4, min_people=1)

    system.add_table(table)

    result = system.remove_table(1)

    assert result is True
    assert len(system.tables) == 0


def test_remove_table_returns_false_for_unknown_table() -> None:
    system = ReservationSystem()
    table = IndoorTable(table_number=1, seats=4, min_people=1)

    system.add_table(table)

    result = system.remove_table(2)

    assert result is False
    assert len(system.tables) == 1


def test_remove_table_fails_when_table_has_reservation() -> None:
    system = ReservationSystem()
    table = IndoorTable(table_number=1, seats=4, min_people=1)
    customer = Customer(name="Max Mustermann", phone_number="0123456789")

    system.add_table(table)

    reservation = system.create_reservation(
        customer=customer,
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=2,
    )

    result = system.remove_table(1)

    assert reservation is not None
    assert result is False
    assert len(system.tables) == 1
    assert system.tables[0] == table


def test_deactivate_table_sets_table_inactive() -> None:
    system = ReservationSystem()
    table = IndoorTable(table_number=1, seats=4, min_people=1)

    system.add_table(table)

    result = system.deactivate_table(1)

    assert result is True
    assert table.is_active is False


def test_activate_table_sets_table_active() -> None:
    system = ReservationSystem()
    table = IndoorTable(table_number=1, seats=4, min_people=1)

    system.add_table(table)
    table.deactivate()

    result = system.activate_table(1)

    assert result is True
    assert table.is_active is True


def test_deactivate_table_fails_when_table_has_active_reservation() -> None:
    system = ReservationSystem()
    table = IndoorTable(table_number=1, seats=4, min_people=1)
    customer = Customer(name="Max Mustermann", phone_number="0123456789")

    system.add_table(table)

    reservation = system.create_reservation(
        customer=customer,
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=2,
    )

    result = system.deactivate_table(1)

    assert reservation is not None
    assert result is False
    assert table.is_active is True
