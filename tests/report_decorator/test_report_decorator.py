# 9 - Testar a geração de uma versão do relatório em cores
# Crie o teste em: tests/report_decorator/test_report_decorator.py
# Uma versão deste relatório será exibida em letreiros em Led, estes letreiros
# são coloridos, para isso, já implementamos o método responsável por retornar
# este relatório em cores.
# Implementamos em : inventory_report/reports/colored_report.py
# Em vez de criarmos uma classe que herda os relatórios originais, utilizamos
# o padrão Decorator para receber o tipo do relatório por composição
# (SimpleReport ou CompleteReport) e, assim, colorir o retorno do método
# generate, que recebe uma lista de produtos e retorna o relatório já colorido.
# Para termos confiança que as cores sairão corretamente, precisamos que você
# implemente o teste, que certifique que o método generate de ColoredReport
# funciona corretamente.

# def generate(self, products_list):
#     report = self.report_type.generate(products_list)
#     index_start = report.find("mais produtos:") + 15
#     index_finish = report.find("\n", index_start)
#     if index_finish == -1:
#         index_finish = len(report)
#     report = (
#         report[:index_start]
#         + "\033[31m"
#         + report[index_start:index_finish]
#         + "\033[0m"
#         + report[index_finish:]
#     )
#     green_phrases = [
#         "Data de fabricação mais antiga:",
#         "Data de validade mais próxima:",
#         "Empresa com mais produtos:",
#     ]
#     for phrase in green_phrases:
#         report = report.replace(
#             phrase,
#             f"\033[32m{phrase}\033[0m",
#         )
#     report_dates = re.findall(r"(\d+-\d+-\d+)", report)

#     for date in report_dates:
#         report = report.replace(
#             date,
#             f"\033[36m{date}\033[0m",
#         )
#     return report

from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
import json

with open("inventory_report/data/inventory.json") as file:
    json_list = json.load(file)


# O nome deste teste deve ser test_decorar_relatorio, ele deve verificar se o
# relatório está devidamente colorido.
def test_decorar_relatorio():
    relatorio_decorado = ColoredReport(SimpleReport).generate(json_list)

    # Para que o Python consiga colorir as strings, é preciso que a string
    # contenha o início do código da cor, e o reset da cor.
    # Execute este print teste em um terminal interativo python3 -i.
    # O resultado das cores podem não ser exatos, por isso, atente-se aos
    # códigos deste exemplo:
    # print("\033[36mAzul\033[0m \033[32mVerde\033[0m \033[31mVermelho\033[0m")

    # O que será verificado pelo avaliador
    # 9 - Deve retornar o relatório devidamente colorido.
    # verde:
    # "Data de fabricação mais antiga:"
    # "Data de validade mais próxima:"
    # "Empresa com mais produtos:"
    # azul: As datas
    # vermelho: Nome da empresa com mais produtos

    # line too long (84 > 79 characters)Flake8(E501)
    mais_antiga = "Data de fabricação mais antiga:"
    mais_proxima = "Data de validade mais próxima:"
    mais_produtos = "Empresa com mais produtos:"
    assert relatorio_decorado == (
        f"\033[32m{mais_antiga}\033[0m \033[36m2020-09-06\033[0m\n"
        f"\033[32m{mais_proxima}\033[0m \033[36m2023-09-17\033[0m\n"
        f"\033[32m{mais_produtos}\033[0m \033[31mTarget Corporation\033[0m"
    )
