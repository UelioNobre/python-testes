from abc import ABC, abstractclassmethod


class InterfaceFormal(ABC):
    @abstractclassmethod
    def exibir_mensagem(self) -> None:
        pass

    def exibir_outra_mensagem(self):
        print("Hello World")


class ClasseConcreta(InterfaceFormal):
    def exibir_mensagem(self):
        print("Olá mundo!")


# teste = InterfaceFormal() - TypeError
teste = ClasseConcreta()
teste.exibir_mensagem()
teste.exibir_outra_mensagem()
