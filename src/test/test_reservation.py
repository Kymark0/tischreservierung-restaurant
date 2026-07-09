from datetime import date as Date
from datetime import time as Time

from customer import Customer
from reservation import Reservation


def test_reservation_stores_attributes() -> None:
    customer = Customer("Max Mustermann", "0123456789")

    reservation = Reservation(
        reservation_id=1,
        customer=customer,
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=4,
        table_number=3
    )

    assert reservation.reservation_id == 1
    assert reservation.customer == customer
    assert reservation.date == Date(2026, 7, 10)
    assert reservation.time == Time(18, 0)
    assert reservation.person_count == 4
    assert reservation.table_number == 3
    assert reservation.status == "aktiv"


def test_cancel_changes_status_to_cancelled() -> None:
    customer = Customer("Max Mustermann", "0123456789")

    reservation = Reservation(
        reservation_id=1,
        customer=customer,
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=4,
        table_number=3
    )

    reservation.cancel()

    assert reservation.status == "storniert"


def test_is_active_returns_true_for_active_reservation() -> None:
    customer = Customer("Max Mustermann", "0123456789")

    reservation = Reservation(
        reservation_id=1,
        customer=customer,
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=4,
        table_number=3
    )

    assert reservation.is_active() is True


def test_is_active_returns_false_for_cancelled_reservation() -> None:
    customer = Customer("Max Mustermann", "0123456789")

    reservation = Reservation(
        reservation_id=1,
        customer=customer,
        date=Date(2026, 7, 10),
        time=Time(18, 0),
        person_count=4,
        table_number=3
    )

    reservation.cancel()

    assert reservation.is_active() is False