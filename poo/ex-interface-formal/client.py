from Printer import Printer
from Seller import Seller
from Manager import Manager
from NotInstanceOfIPerson import NotInstanceOfIPerson


seller = Seller("Vendedor")
manager = Manager("Gerente")
not_instance_of_iperson = NotInstanceOfIPerson("People")


Printer.imprime_cargo(seller)
Printer.imprime_cargo(manager)

Printer.imprime_cargo(not_instance_of_iperson)
