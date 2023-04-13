# 8 - Testar o relatório individual do produto
# Crie o teste em: tests/product_report/test_product_report.py
# Boa novidade, o primeiro relatório já implementamos neste arquivo
# inventory_report/inventory/product.py. Formulamos uma frase construída com
# as informações do produto, que será muito útil para etiquetarmos o estoque.
# Para desenvolver este relatório, utilizamos o recurso __repr__ do Python,
# que permite alterar a representatividade do objeto, para que sempre que
# usarmos um print nele, no lugar de endereço de memória, teremos uma String
# personalizada.
# Dica: A reimplementação do __repr__ não faz o objeto retornar exatamente uma
# string, fazer um cast para string, pode te ajudar.
# Exemplo da frase:
# O produto farinha fabricado em 01-05-2021 por Farinini com validade até
# 02-06-2023 precisa ser armazenado ao abrigo de luz.
# Agora para mantermos uma boa cobertura de testes, precisamos que você
# implemente o teste.
# O nome deste teste deve ser test_relatorio_produto, ele deve instanciar um
# objeto Product e verificar se acessá-lo a frase de retorno esta correta.

# def __repr__(self):
#     return (
#         f"O produto {self.nome_do_produto}"
#         f" fabricado em {self.data_de_fabricacao}"
#         f" por {self.nome_da_empresa} com validade"
#         f" até {self.data_de_validade}"
#         f" precisa ser armazenado {self.instrucoes_de_armazenamento}."
#     )

# from inventory_report.inventory.product import Product


def test_relatorio_produto():
    pass  # Seu teste deve ser escrito aqui
