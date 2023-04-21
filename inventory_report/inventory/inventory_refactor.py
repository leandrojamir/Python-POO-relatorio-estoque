# Requisitos bônus
# 10 - Criar uma classe InventoryIterator
#  A classe Inventory deverá ser refatorada (copiada) em outro arquivo chamado
# inventory_report/inventory/inventory_refactor.py. Nesse arquivo você irá
# refatorar a classe Inventory chamando-a de InventoryRefactor.
# import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
# import json
# import xml.etree.ElementTree as ET
from inventory_report.inventory.inventory_iterator import InventoryIterator
from collections.abc import Iterable


class InventoryRefactor(Iterable):
    #  A classe InventoryRefactor deve utilizar as classes definidas no
    # requisito 8 (na verdade 7) para lidar com a lógica de importação, via
    # composição no método import_data.
    #  A classe InventoryRefactor deve receber por seu construtor a classe que
    # será utilizada para lidar com a lógica de importação e armazenar em um
    # atributo chamado importer.
    #  A classe InventoryRefactor deve ter um método de instância que recebe um
    # caminho para o arquivo a ser importado, e carrega seus dados.
    #  Ao importar os dados, os mesmos devem ser armazenados na instância, em
    # adição aos itens já presentes naquela instância. O atributo de
    # InventoryRefactor que armazena esses dados deve se chamar data.
    #  A classe InventoryIterator deverá implementar a interface de um iterator
    # (Iterator) com o método __next__. Além disso, a classe InventoryRefactor
    # deve implementar o método __iter__, que retornará este iterador.
    #  As classes InventoryIterator e InventoryRefactor devem implementar
    # corretamente a interface do padrão de projeto Iterator, de modo que seja
    # possível iterar sobre os itens em estoque.
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    # O método receberá como primeiro parâmetro uma string como caminho para o
    # arquivo CSV e como segundo parâmetro uma string que representa o tipo de
    # relatório a ser gerado.
    def import_data(self, path: str, type: str):
        result = InventoryRefactor.gerar_relatorio(
            self.recuperar_dados_csv_json_xml(path), type
        )

        return result

    # De acordo com os parâmetros recebidos, deve recuperar os dados do
    # arquivo e chamar o método de gerar relatório correspondente à entrada
    # passada. Ou seja, o método da classe Inventory deve chamar o método
    # generate da classe que vai gerar o relatório
    # (SimpleReport, CompleteReport).
    @classmethod
    def gerar_relatorio(cls, list: list[dict], type: str):
        # type terão tipos: "simples" e "completo"
        if type == "simples":
            relatorio = SimpleReport.generate(list)
        else:
            relatorio = CompleteReport.generate(list)

        return relatorio

    # @classmethod
    def recuperar_dados_csv_json_xml(self, nome_arquivo: str):
        print(f"\nvvv\nImporter{self.importer}")
        # <class 'inventory_report.importer.csv_importer.CsvImporter'>
        data_list = self.importer.import_data(nome_arquivo)
        print(f"\nvvv\ndados_csv_json_xml{data_list}")
        for info in data_list:
            self.data.append(info)

        return self.data
