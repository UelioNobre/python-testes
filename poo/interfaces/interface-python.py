class InterfaceFuncionario:
    def calcular_salario(self) -> str:
        raise NotImplementedError(
            "Implemente o método calcular_salario na classe concreta"
        )


class Funcionario(InterfaceFuncionario):
    def calcular_salario(self):
        return "Um calculo foi realizado"


funcionario1 = Funcionario()
salario = funcionario1.calcular_salario()
print(f"Operacao para calcular salario: {salario}")
