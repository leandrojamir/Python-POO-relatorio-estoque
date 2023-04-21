# Requisitos bônus
# 10 - Criar uma classe InventoryIterator
# Crie em: inventory_report/inventory/inventory_iterator.py

#  O estoque será mostrado por painéis de led. Para não sobrecarregarmos a
# memória destes painéis, queremos poder iterar pelos itens do estoque, um
# item por vez. Para isso, precisamos primeiro refatorar a forma com que
# importamos os dados, e então aplicar o Padrão Iterator.

# Os atributos e os métodos devem ser públicos.
from collections.abc import Iterator


#  A classe InventoryIterator deverá implementar a interface de um iterator
# (Iterator) com o método __next__. Além disso, a classe InventoryRefactor
# deve implementar o método __iter__, que retornará este iterador.
#  As classes InventoryIterator e InventoryRefactor devem implementar
# corretamente a interface do padrão de projeto Iterator, de modo que seja
# possível iterar sobre os itens em estoque.
class InventoryIterator(Iterator):
    def __init__(self, item):
        self._item = item
        self._pos = 0

    def __next__(self):
        try:
            result = self._item[self._pos]
        except IndexError:
            raise StopIteration()
        else:
            self._pos += 1
            return result


# class IteradorDoBaralho(Iterator):
#     def __init__(self, cartas):
#         self._cartas = cartas
#         self._pos = 0

#     def __next__(self):
#         try:
#             carta = self._cartas[self._pos]
#         except IndexError:
#             raise StopIteration()
#         else:
#             self._pos += 1
#             return carta
