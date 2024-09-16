from IPerson import IPerson


class Seller(IPerson):
    def __init__(self, role: str) -> None:
        super().__init__(role)

    def print_role(self) -> None:
        print(self.role)
