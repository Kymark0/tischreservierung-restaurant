class Customer:
    """Represents a customer who can make a reservation."""

    def __init__(self, name: str, phone_number: str, email: str = "") -> None:
        """Create a customer with name, phone number and optional email."""
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def get_info(self) -> str:
        """Return the customer information as a formatted string."""
        if self.email:
            return (
                f"{self.name}, "
                f"Telefon: {self.phone_number}, "
                f"E-Mail: {self.email}"
            )

        return f"{self.name}, Telefon: {self.phone_number}"