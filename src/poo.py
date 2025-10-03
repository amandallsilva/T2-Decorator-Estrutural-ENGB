## Código orientado a objetos - Decorator

# Classe base
class PizzaComum:  # Pizza simples sem cobertura, base para os decoradores
    def descricao(self):
        return "Pizza Comum"
    def custo(self):
        return 10

# Decorador: Queijo
class Queijo:  # Recebe um objeto pizza como parâmetro; adiciona queijo sem criar subclasses para cada tipo de pizza
    def __init__(self, pizza):
        self._pizza = pizza

    def descricao(self):  # Construída dinamicamente: pega a descrição da pizza encapsulada e adiciona "Queijo"
        return self._pizza.descricao() + ", Queijo"

    def custo(self):  # Adiciona 2 ao custo da pizza encapsulada
        return self._pizza.custo() + 2  

# Decorador: Calabresa
class Calabresa:  # Construída dinamicamente: pega a pizza passada e adiciona Calabresa
    def __init__(self, pizza):
        self._pizza = pizza

    def descricao(self):
        return self._pizza.descricao() + ", Calabresa"

    def custo(self): 
        return self._pizza.custo() + 3

# Testando
pizza_simples = PizzaComum()
pizza_queijo = Queijo(pizza_simples)  # Cria uma pizza com queijo empilhando o decorador sobre a pizza comum
pizza_queijo_calabresa = Calabresa(pizza_queijo)  # Cria uma pizza com queijo e calabresa empilhando decoradores

# Impressão dos resultados
print(pizza_simples.descricao(), "-", pizza_simples.custo())              # Pizza Comum - 10
print(pizza_queijo.descricao(), "-", pizza_queijo.custo())                # Pizza Comum, Queijo - 12
print(pizza_queijo_calabresa.descricao(), "-", pizza_queijo_calabresa.custo())  # Pizza Comum, Queijo, Calabresa - 15

