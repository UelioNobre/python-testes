from Printer import Printer
from Seller import Seller
from Manager import Manager
from NotInstanceOfIPerson import NotInstanceOfIPerson
import traceback


seller = Seller("Vendedor")
manager = Manager("Gerente")
not_instance_of_iperson = NotInstanceOfIPerson("People")


Printer.imprime_cargo(seller)
Printer.imprime_cargo(manager)

try:
    Printer.imprime_cargo(not_instance_of_iperson)
except Exception as err:
    print("\n")
    print(f"Error:: {err}")
    print(traceback.format_exc())
    print("\n")
