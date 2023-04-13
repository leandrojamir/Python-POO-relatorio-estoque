# 7 - Organizar o código de importação com o padrão Strategy
# Crie em: inventory_report/importer/importer.py
# Como pôde observar até aqui, o método import_data está com muitas
# responsabilidades, e, com o intuito de resolver isso, podemos dividir a sua
# complexidade para cada formato de arquivo.
# O padrão de projeto Strategy nos ajuda a isolar cada estratégia em um objeto,
# e por meio de uma Interface podemos padronizar a assinatura dos métodos,
# garantindo que todas elas possuam o comportamento similar.
# Ao rodar os testes localmente, você terá um teste para cada validação de
# cada informação
from abc import ABC, abstractmethod


# Crie uma classe abstrata "Importer" para ser a interface da estratégia
class Importer(ABC):
    # A classe abstrata deve definir a assinatura do método "import_data" a ser
    # implementado por cada classe herdeira. Esse método deve ser estático ou
    # de classe e deve receber como parâmetro o nome do arquivo a ser importado
    @abstractmethod
    def import_data(nome_arquivo: str):
        raise NotImplementedError

    @abstractmethod
    def recuperar_dados_csv_json_xml(nome_arquivo: str):
        raise NotImplementedError
