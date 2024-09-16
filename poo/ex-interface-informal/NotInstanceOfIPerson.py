class NotInstanceOfIPerson:
    def __init__(self, role: str) -> None:
        self.role = role

    def print_role(self) -> None:
        print(self.role)
