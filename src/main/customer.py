class Customer:
    def __init__(self, name: str, phone_number: str, email: str = "") -> None:
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def get_info(self) -> str:
        # TODO: Kundendaten formatiert zurückgeben.
        pass