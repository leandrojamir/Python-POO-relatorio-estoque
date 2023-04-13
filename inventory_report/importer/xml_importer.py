# 7 - Organizar o código de importação com o padrão Strategy
# A Interface será uma classe abstrata "Importer" terá três classes de
# estratégias herdeiras: "CsvImporter", "JsonImporter" e "XmlImporter".
# Crie as classes nos respectivos arquivos:
# inventory_report/importer/csv_importer.py
# inventory_report/importer/json_importer.py
# inventory_report/importer/xml_importer.py
import xml.etree.ElementTree as ET
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(nome_arquivo: str):
        return XmlImporter.recuperar_dados_csv_json_xml(nome_arquivo)

    @classmethod
    # Deve lançar uma exceção do tipo "ValueError" caso a extensão do arquivo
    # passado por parâmetro seja inválida.
    def recuperar_dados_csv_json_xml(cls, path: str):
        if path.endswith("xml"):
            tree = ET.parse(path)
            root = tree.getroot()
            xml_list = [
                {x.tag: x.text for x in list}
                for list in root
            ]
            return xml_list
        else:
            # A mensagem de erro da exceção deve ser "Arquivo inválido".
            raise ValueError("Arquivo inválido")
