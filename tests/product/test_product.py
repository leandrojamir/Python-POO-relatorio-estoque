# 1 - Testar o construtor/inicializador do objeto Produto
# Ao analisar o código do projeto, você encontrará a classe do objeto produto
# já implementada neste arquivo:
# inventory_report/inventory/product.py, a classe Product.

# Para termos confiança em continuar as implementações, precisamos que você
# implemente o teste, que certifique que o método __init__ da classe Product
# esta funcionando corretamente.

# class Product:
#     def __init__(
#         self,
#         id,
#         nome_do_produto,
#         nome_da_empresa,
#         data_de_fabricacao,
#         data_de_validade,
#         numero_de_serie,
#         instrucoes_de_armazenamento,
#     ):
#         self.id = id
#         self.nome_do_produto = nome_do_produto
#         self.nome_da_empresa = nome_da_empresa
#         self.data_de_fabricacao = str(data_de_fabricacao)
#         self.data_de_validade = str(data_de_validade)
#         self.numero_de_serie = numero_de_serie
#         self.instrucoes_de_armazenamento = instrucoes_de_armazenamento

from inventory_report.inventory.product import Product


# O nome deste teste deve ser test_cria_produto,
def test_cria_produto():
    init_product = Product(
        11,
        "Titanium Dioxide II",
        "Target Corporation",
        "2020-12-08",
        "2023-12-08",
        "FR29 5791 5333 58XR G4PR IG28 D08",
        "instrucao 11",
    )
    # ele deve verificar o correto preenchimento dos seguintes atributos:
    # id (int)
    assert init_product.id == 11
    # nome_da_empresa (string)
    assert init_product.nome_da_empresa == "Target Corporation"
    # nome_do_produto (string)
    assert init_product.nome_do_produto == "Titanium Dioxide II"
    # data_de_fabricacao (string)
    assert init_product.data_de_fabricacao == "2020-12-08"
    # data_de_validade (string)
    assert init_product.data_de_validade == "2023-12-08"
    # numero_de_serie (string)
    assert init_product.numero_de_serie == "FR29 5791 5333 58XR G4PR IG28 D08"
    # instrucoes_de_armazenamento (string)
    assert init_product.instrucoes_de_armazenamento == "instrucao 11"
