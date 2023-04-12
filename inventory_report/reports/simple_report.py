# 2 - Gerar a versão simplificada do relatório
# Crie a classe em: inventory_report/reports/simple_report.py
# Dica: O módulo datetime pode te ajudar.
from datetime import date


class SimpleReport:

    # O relatório deve ser gerado através de um método estático ou de classe
    @staticmethod
    # chamado generate escrito dentro da classe SimpleReport.
    def generate(stock):

        # Ao rodar os testes localmente, você terá um teste para cada validação
        # de cada informação
        # @pytest.mark.dependency()
        # def test_validar_simplereport_retorna_data_de_fabricacao_mais_antiga(
        #   stock
        # ):
        #  for stk in itertools.permutations(stock):
        #    report = SimpleReport.generate(list(stk))  # type: ignore
        #    assert f"Data de fabricação mais antiga: {oldest_date}" in report

        mais_antiga = SimpleReport.retorna_data_de_fabricacao_mais_antiga(
            stock
        )
        mais_proxima = SimpleReport.retorna_validade_mais_proxima(stock)
        mais_produtos = SimpleReport.retorna_empresa_com_maior_estoque(stock)

        # O método deverá retornar uma string de saída com o seguinte formato:
        return (
            # Data de fabricação mais antiga: YYYY-MM-DD
            f"Data de fabricação mais antiga: {mais_antiga}\n"
            # Data de validade mais próxima: YYYY-MM-DD
            f"Data de validade mais próxima: {mais_proxima}\n"
            # Empresa com mais produtos: NOME DA EMPRESA
            f"Empresa com mais produtos: {mais_produtos}"
        )

    # Deve ser possível executar o método generate sem instanciar um objeto
    # de SimpleReport
    @classmethod
    # O método deve receber um parâmetro que representa
    # uma list (estrutura de dados), onde cada posição contém
    # um dict(estrutura de dados).
    def retorna_data_de_fabricacao_mais_antiga(cls, list: list[dict]):

        # Exemplo de formato de entrada
        #    [
        #      {
        #        "id": 1,
        #        "nome_do_produto": "CADEIRA",
        #        "nome_da_empresa": "Forces of Nature",
        #        "data_de_fabricacao": "2022-04-04",
        #        "data_de_validade": "2023-02-09",
        #        "numero_de_serie": "FR48",
        #        "instrucoes_de_armazenamento": "Conservar em local fresco"
        #      }
        #    ]

        # classmethod date.fromisoformat(date_string)¶
        # Retorna um date correspondendo a date_string
        # fornecido no formato YYYY-MM-DD:
        data_de_fabricacao = date.fromisoformat(list[0]["data_de_fabricacao"])
        for item in list:
            data_de_fabricacao_item = date.fromisoformat(
                item["data_de_fabricacao"]
            )
            if data_de_fabricacao < data_de_fabricacao_item:
                return data_de_fabricacao
            else:
                data_de_fabricacao = data_de_fabricacao_item

        return data_de_fabricacao

    @classmethod
    # O método deve receber um parâmetro que representa
    # uma list (estrutura de dados), onde cada posição contém
    # um dict(estrutura de dados).
    def retorna_validade_mais_proxima(cls, list: list[dict]):

        # A data de validade mais próxima, somente considera itens que ainda
        # não venceram
        data_validade = [
            item["data_de_validade"] for item in list
            if item["data_de_validade"] >= date.today().isoformat()
        ]
        return min(data_validade)

    @classmethod
    # O método deve receber um parâmetro que representa
    # uma list (estrutura de dados), onde cada posição contém
    # um dict(estrutura de dados).
    def retorna_empresa_com_maior_estoque(cls, list: list[dict]):
        # posso fazer um count manual e pegar a max()
        estoque = dict()
        for item in list:
            item_empresa = item["nome_da_empresa"]
            if item_empresa in estoque:
                estoque[item_empresa] = estoque[item_empresa] + 1
            else:
                estoque[item_empresa] = 0
        empresa_mais_produtos = max(estoque, key=estoque.get)

        return empresa_mais_produtos


# tests/test_simple_report.py::
# test_validar_simplereport_retorna_data_de_fabricacao_mais_antiga PASSED
# tests/test_simple_report.py::
# test_validar_simplereport_retorna_validade_mais_proxima PASSED
# tests/test_simple_report.py::
# test_validar_simplereport_retorna_empresa_com_maior_estoque PASSED
# tests/test_simple_report.py::
# test_metodo_generate_de_simplereport_retorna_informacoes_simples PASSED
# tests/test_simple_report.py::
# test_validar_simplereport_retorna_formato_correto PASSED
