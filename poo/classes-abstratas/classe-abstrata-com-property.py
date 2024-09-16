from abc import ABC, abstractmethod


class ClasseAbstrata(ABC):
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    @abstractmethod
    def name(self) -> str:
        return self._name


class ClasseConcreta(ClasseAbstrata):
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def name(self) -> str:
        return super().name


testeClasseAbstrata = ClasseConcreta("Uélio")
print(testeClasseAbstrata.name())
