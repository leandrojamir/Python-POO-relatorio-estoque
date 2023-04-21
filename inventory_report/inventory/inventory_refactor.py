# Requisitos bônus
# 10 - Criar uma classe InventoryIterator
#  A classe Inventory deverá ser refatorada (copiada) em outro arquivo chamado
# inventory_report/inventory/inventory_refactor.py. Nesse arquivo você irá
# refatorar a classe Inventory chamando-a de InventoryRefactor.
import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import json
import xml.etree.ElementTree as ET
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

    # O método deve ser estático ou de classe, ou seja, deve ser possível
    # chamá-lo sem instanciar um objeto da classe.
    @staticmethod
    # O método receberá como primeiro parâmetro uma string como caminho para o
    # arquivo CSV e como segundo parâmetro uma string que representa o tipo de
    # relatório a ser gerado.
    def import_data(path: str, type: str):
        result = InventoryRefactor.gerar_relatorio(
            InventoryRefactor.recuperar_dados_csv_json_xml(path), type
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

    @classmethod
    # import csv
    # # lê os dados
    # with open("graduacao_unb.csv", encoding = "utf-8") as file:
    #     graduacao_reader = csv.DictReader(file, delimiter=",", quotechar='"')
    #     # a linha de cabeçalhos é utilizada como chave do dicionário
    #     # agrupa cursos por departamento
    #     group_by_department = {}
    #     for row in graduacao_reader:
    #         department = row["unidade_responsavel"]
    #         if department not in group_by_department:
    #             group_by_department[department] = 0
    #         group_by_department[department] += 1
    def recuperar_dados_csv_json_xml(cls, path: str):
        if path.endswith("csv"):
            with open(path, encoding="utf-8") as file:
                csv_reader = csv.DictReader(file, delimiter=",", quotechar='"')
                csv_list = []
                for lista in csv_reader:
                    csv_list.append(lista)

                return csv_list
        # import json
        # # leitura de todos os pokemons
        # with open("pokemons.json") as file:
        #     pokemons = json.load(file)["results"]
        if path.endswith("json"):
            with open(path) as file:
                json_list = json.load(file)

                return json_list
        # https://pt.stackoverflow.com/questions/3561/como-criar-e-ler-um-xml-com-python
        # >>> import xml.etree.ElementTree as ET
        # >>> tree = ET.parse('country_data.xml')
        # >>> root = tree.getroot()
        # >>> [(x.tag, x.attrib) for x in root] # Lista os elementos filhos:
        # nome e atributos
        # [('country', {'name':'Liechtenstein'}), (...), (...)]
        if path.endswith("xml"):
            tree = ET.parse(path)
            root = tree.getroot()
            # aqui esta sendo usado list comprehension praticamente igual ao
            # exemplo do stackoberflow porque o linter acusava erro
            # 'Inventory.recuperar_dados_csv_json_xml' is too complex
            # (7)Flake8(C901)
            # https://medium.com/data-hackers/aprenda-list-comprehension-7335844265bd#:~:text=List%20Comprehension%20nada%20mais%20%C3%A9,resultados%20em%20uma%20nova%20lista.
            # xml_list = []
            # for list in root:
            #     dict = {}
            #     for x in list:
            #         dict[x.tag] = x.text
            #     xml_list.append(dict)
            xml_list = [{x.tag: x.text for x in list} for list in root]
            return xml_list
