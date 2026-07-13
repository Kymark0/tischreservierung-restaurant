from customer import Customer


def test_customer_stores_attributes() -> None:
    customer = Customer(
        name="Max Mustermann",
        phone_number="0123456789",
        email="max@example.com",
    )

    assert customer.name == "Max Mustermann"
    assert customer.phone_number == "0123456789"
    assert customer.email == "max@example.com"


def test_customer_email_is_optional() -> None:
    customer = Customer(name="Max Mustermann", phone_number="0123456789")

    assert customer.email == ""
