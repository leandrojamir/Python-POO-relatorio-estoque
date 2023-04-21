# 7 - Organizar o código de importação com o padrão Strategy
# A Interface será uma classe abstrata "Importer" terá três classes de
# estratégias herdeiras: "CsvImporter", "JsonImporter" e "XmlImporter".
# Crie as classes nos respectivos arquivos:
# inventory_report/importer/csv_importer.py
# inventory_report/importer/json_importer.py
# inventory_report/importer/xml_importer.py
import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(nome_arquivo: str):
        # O método deverá ler os dados do arquivo passado e retorná-los
        # estruturados em uma lista de dicionários conforme exemplo abaixo:
        # [
        #   {
        #     "id": 1,
        #     "nome_do_produto": "Cafe",
        #     "nome_da_empresa": "Cafes Nature",
        #     "data_de_fabricacao": "2020-07-04",
        #     "data_de_validade": "2023-02-09",
        #     "numero_de_serie": "FR48",
        #     "instrucoes_de_armazenamento": "instrucao"
        #   }
        # ]
        return CsvImporter.recuperar_dados_csv_json_xml(nome_arquivo)

    @classmethod
    def recuperar_dados_csv_json_xml(cls, path: str):
        # O método "import_data" definido por cada classe herdeira deve lançar
        # uma exceção do tipo "ValueError" caso a extensão do arquivo passado
        # por parâmetro seja inválida. Por exemplo, quando se passa um caminho
        # de um arquivo com extensão ".csv" para o "JsonImporter".
        if path.endswith("csv"):
            with open(path, encoding="utf-8") as file:
                csv_reader = csv.DictReader(file, delimiter=",", quotechar='"')
                csv_list = []
                for lista in csv_reader:
                    csv_list.append(lista)

                return csv_list
        else:
            # A mensagem de erro da exceção deve ser "Arquivo inválido".
            raise ValueError("Arquivo inválido")


# [{'id': '1', 'nome_do_produto': 'Nicotine Polacrilex', 'nome_da_empresa':
# 'Target Corporation', 'data_de_fabricacao': '2021-02-18', 'data_de_validade':
# '2023-09-17', 'numero_de_serie': 'CR25 1551 4467 2549 4402 1',
# 'instrucoes_de_armazenamento': 'instrucao 1'},
# {'id': '10', 'nome_do_produto': 'Titanium Dioxide', 'nome_da_empresa':
# 'Target Corporation', 'data_de_fabricacao': '2020-12-08', 'data_de_validade':
# '2023-12-08', 'numero_de_serie': 'FR29 5791 5333 58XR G4PR IG28 D08',
# 'instrucoes_de_armazenamento': 'instrucao 10'}]
