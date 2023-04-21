# 11 - Preencha a função main no módulo inventory_report/main.py
#  Ao chamar o comando no formato abaixo pelo terminal, deve ser impresso na
#  tela o devido relatório no formato da saída dos requisitos 3 e 4:
# inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>

#  Deverá ser usado a classe InventoryRefactor para recuperar os dados e gerar
# o relatório.
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter

#  Ao utilizar algo do módulo sys, faça a importação com import sys e utilize
# sys.xxxx (onde xxxx é o que você quer utilizar). Não faça
# from sys import xxxx, pois isso pode fazer com que os testes não passem.
# from sys import argv, stdout, stderr
import sys


def main():
    try:
        #  Essa função deve, ao receber pela linha de comando o caminho de um
        # arquivo e o tipo de relatório, devolver o relatório correto.
        #  Você pode utilizar o sys.argv para receber a entrada de dados da
        # pessoa usuária.
        # caminho, tipo = argv[1], argv[2]
        caminho, tipo = sys.argv[1], sys.argv[2]
        if caminho.endswith("csv"):
            get_csv = InventoryRefactor(CsvImporter)
            # csv_list = stdout.write(get_csv.import_data(caminho, tipo))
            csv_list = sys.stdout.write(get_csv.import_data(caminho, tipo))

            return csv_list

        elif caminho.endswith("json"):
            get_json = InventoryRefactor(JsonImporter)
            # json_list = stdout.write(get_json.import_data(caminho, tipo))
            json_list = sys.stdout.write(get_json.import_data(caminho, tipo))

            return json_list

        else:
            get_xml = InventoryRefactor(XmlImporter)
            # xml_list = stdout.write(get_xml.import_data(caminho, tipo))
            xml_list = sys.stdout.write(get_xml.import_data(caminho, tipo))

            return xml_list
    #  Caso a chamada tenha menos de dois argumentos exiba a mensagem de erro
    # "Verifique os argumentos" na stderr.
    except IndexError:
        # stderr.write("Verifique os argumentos\n")
        sys.stderr.write("Verifique os argumentos\n")


# Dicas:
#  Se o comando não encontrar o pacote inventory_report, basta executar pip
# install . na raiz do projeto.
#  Tome a precaução de não deixar um print() em seu código, pois ele irá
# conflitar com os testes.
# Teste manual
#  No ambiente virtual onde seu projeto foi configurado, instale o próprio
# projeto com o comando pip install . (a cada alteração refazer pip install .)
# Agora execute o projeto com:
# inventory_report parametro_1 parametro_2
# exemplo:
# inventory_report inventory_report/data/inventory.csv simples
# Desta forma você conseguirá interagir gerar o relatório com o comando.

# (.venv) jamir@jamir-X550CA:~/Projetos/computer-science/sd-023-b-inventory
# -report$ inventory_report inventory_report/data/inventory.csv simples
# Data de fabricação mais antiga: 2020-09-06
# Data de validade mais próxima: 2023-09-17
# Empresa com mais produtos: Target Corporation(.venv)
