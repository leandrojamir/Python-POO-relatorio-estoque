# 4 - Gere os relatórios através de um arquivo CSV
# Crie em: inventory_report/inventory/inventory.py
import csv
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
# 5 - Gere os relatórios através de um arquivo JSON
# Utilize o mesmo método do requisito anterior.
# Altere o método import_data para que ele também seja capaz de carregar
# arquivos JSON.
# Como no requisito anterior, o método ainda receberá como primeiro parâmetro
# uma string como caminho para o arquivo, e como segundo parâmetro uma string
# que representa o tipo de relatório a ser gerado. Tipos:
# "simples"
# "completo"
# De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e
# chamar o método de gerar relatório correspondente à entrada passada.
# Ou seja, o método da classe Inventory deve chamar o método generate da
# classe que vai gerar o relatório (SimpleReport, CompleteReport).
import json


# A importação do arquivo CSV deve ser realizada através do método
# "import_data" que você deve criar em uma classe chamada Inventory.
class Inventory:
    # O método deve ser estático ou de classe, ou seja, deve ser possível
    # chamá-lo sem instanciar um objeto da classe.
    @staticmethod
    # O método receberá como primeiro parâmetro uma string como caminho para o
    # arquivo CSV e como segundo parâmetro uma string que representa o tipo de
    # relatório a ser gerado.
    def import_data(path: str, type: str):
        result = Inventory.gerar_relatorio(
            Inventory.recuperar_dados_arquivo(path), type
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
    def recuperar_dados_arquivo(cls, path: str):
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


# tests/test_inventory.py::
# test_validar_importerdata_importar_um_arquivo_csv_simples PASSED
# tests/test_inventory.py::
# test_validar_importerdata_importar_um_arquivo_csv_completo PASSED
# tests/test_inventory.py::
# test_importe_arquivos_CSV_pelo_metodo_import_data PASSED

# tests/test_inventory.py::
# test_validar_importerdata_importar_um_arquivo_json_simples PASSED
# tests/test_inventory.py::
# test_validar_importerdata_importar_um_arquivo_json_completo PASSED
# tests/test_inventory.py::
# test_importe_arquivos_JSON_pelo_metodo_import_data PASSED
