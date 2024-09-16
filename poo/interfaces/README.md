# Interfaces

Diferente de outras linguagens de programação, Python não tem uma palavra 
reservada para criação de interfaces.

O que é possível fazer é declara um método que lança uma exceção caso não 
seja implementado nas classes filhas. Mas isso se encaixa em um tipo conceitual de interfaces (informais)

Um ponto importante a se observar: Só será avisado que deve implementar um método de uma interface informal, quando houver uma chamada à uma assinatura do método. Diferente das interfaces formais (classes abstratas). 

_Na seção Interface Formal vs Informal há mais detalhes._

### Classes abstratas

Classes abtratas (pode-se também de chamadas de interfaces), por outro lado não são instanciadas.

Para que uma classe seja considerada "abstrata", em Python, ele deve herdar da classe ABC, presente no módulo abc, disponível na linguagem. ABC significa abstract base class (Classe Abstrata Base).

_Na seção Interface Formal vs Informal há mais detalhes._

### Interface Formal vs Informal

Em Python, a distinção entre uma interface formal e uma informal geralmente se refere à diferença entre herança de classes (interface formal) e a implementação de métodos específicos esperados (interface informal). Ambos os conceitos são importantes em Python, mas são abordados de maneiras um pouco diferentes. Algumas vezes é utilizada sem nenhum decorator.

#### Interface Formal (Herança de Classes):

Em uma interface formal, você usa herança de classes para definir uma relação entre uma classe base (ou uma classe abstrata) e suas subclasses. A classe base pode ter métodos abstratos que as subclasses devem implementar.
Em Python, você pode usar o módulo abc (Abstract Base Classes) para criar classes abstratas que definem interfaces formais. Essas classes abstratas podem ter métodos abstratos que devem ser implementados pelas subclasses.

Exemplo:

```python
from abc import ABC, abstractmethod

class InterfaceFormal(ABC):
    @abstractmethod
    def metodo_abstrato(self):
        pass

class MinhaClasseConcreta(InterfaceFormal):

    # Não implementar ese método, um erro aparecerá
    def metodo_abstrato(self):
        print("Implementação do método abstrato")

instancia = MinhaClasseConcreta()
instancia.metodo_abstrato()  # Chama o método implementado
```


#### Interface Informal (Protocolo Duck Typing):

Em uma interface informal, não há uma classe base formal, mas sim a expectativa de que uma determinada interface (conjunto de métodos) será suportada por um objeto.

Python segue o princípio do "duck typing", que significa que o tipo de um objeto é determinado pelos métodos e atributos que ele possui, em vez de sua herança de uma classe específica.

Exemplo:
```python
class InterfaceInformal:
    def metodo_informal(self):
        pass

class MinhaClasseConcreta:
    def metodo_informal(self):
        print("Implementação do método informal")

instancia = MinhaClasseConcreta()
instancia.metodo_informal()  # Chama o método informal

```