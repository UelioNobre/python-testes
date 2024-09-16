from IPerson import IPerson
from typing import Any


class Printer:
    @staticmethod
    def imprime_cargo(instance: Any):
        if not isinstance(instance, IPerson):
            raise TypeError("Invalid instance type")
        else:
            instance.print_role()
