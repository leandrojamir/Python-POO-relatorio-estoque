# 3 - Gerar a versão completa do relatório
# Crie em: inventory_report/reports/complete_report.py

from inventory_report.reports.simple_report import SimpleReport


# A classe CompleteReport deve herdar da classe SimpleReport e sobrescrever o
# método generate, de modo a especializar seu comportamento.
class CompleteReport(SimpleReport):
    # O relatório deve ser gerado através de um método generate para a classe
    # CompleteReport.
    @staticmethod
    def generate(stock):
        mais_antiga = SimpleReport.retorna_data_de_fabricacao_mais_antiga(
            stock
        )
        mais_proxima = SimpleReport.retorna_validade_mais_proxima(stock)
        mais_produtos = SimpleReport.retorna_empresa_com_maior_estoque(stock)
        estoque_empresa = CompleteReport.retorna_quantidade_de_estoque_correto(
            stock
        )

        # O método deverá retornar uma saída com o seguinte formato:
        return (
            # Data de fabricação mais antiga: YYYY-MM-DD
            f"Data de fabricação mais antiga: {mais_antiga}\n"
            # Data de validade mais próxima: YYYY-MM-DD
            f"Data de validade mais próxima: {mais_proxima}\n"
            # Empresa com mais produtos: NOME DA EMPRESA
            f"Empresa com mais produtos: {mais_produtos}\n"
            # Produtos estocados por empresa:
            # - Physicians Total Care, Inc.: QUANTIDADE
            # - Newton Laboratories, Inc.: QUANTIDADE
            # - Forces of Nature: QUANTIDADE
            f"Produtos estocados por empresa:\n"
            f"{estoque_empresa}\n"
        )

    # Deve ser possível executar o método generate sem instanciar um objeto de
    # CompleteReport
    @classmethod
    # O método deve receber de parâmetro uma lista de dicionários no seguinte
    # formato:
    # [
    #   {
    #     "id": 1,
    #     "nome_do_produto": "MESA",
    #     "nome_da_empresa": "Forces of Nature",
    #     "data_de_fabricacao": "2022-05-04",
    #     "data_de_validade": "2023-02-09",
    #     "numero_de_serie": "FR48",
    #     "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
    #   }
    # ]
    # Ele deverá receber dados numa lista contendo estruturas do
    # tipo dict e deverá retornar uma string formatada como um relatório.
    def retorna_quantidade_de_estoque_correto(cls, list: list[dict]):
        stock = dict()
        for item in list:
            empresa_item = item["nome_da_empresa"]
            if empresa_item in stock:
                stock[empresa_item] = stock[empresa_item] + 1
            else:
                stock[empresa_item] = 1

        estoque_empresa = []
        for nome_da_empresa in stock:
            # - Forces of Nature: QUANTIDADE
            estoque_empresa.append(
                f"- {nome_da_empresa}: {stock[nome_da_empresa]}"
            )
            result = "\n".join(estoque_empresa)

        return result


# tests/test_complete_report.py::
# test_validar_completereport_retorna_data_de_fabricacao_mais_antiga PASSED
# tests/test_complete_report.py::
# test_validar_completereport_retorna_validade_mais_proxima PASSED
# tests/test_complete_report.py::
# test_validar_completereport_retorna_empresa_com_maior_estoque PASSED
# tests/test_complete_report.py::
# test_validar_completereport_retorna_quantidade_de_estoque_correto PASSED
# tests/test_complete_report.py::
# test_validar_completereport_retorna_formato_correto PASSED
# tests/test_complete_report.py::
# test_metodo_generate_de_completereport_retorna_informacoes_completas PASSED
