from abc import ABC, abstractmethod


class Computador(ABC):
    @abstractmethod
    def operacao(self):
        print("Realiza uma operacao")


class Somar(Computador):
    def operacao(self, a, b):
        super().operacao()
        print(f"É uma operação de soma: a={a}, b={b}")
        return a + b


computa = Somar()
resultado_soma = computa.operacao(2, 3)
print(f"Resultado da soma: {resultado_soma}")
