# Boas-vindas ao repositório do Inventory Reports

<details>
  <summary><strong>👨‍💻 O que deverá ser desenvolvido</strong></summary><br />

  Neste projeto nós vamos fazer algo parecido, mas utilizando a Programação Orientada a Objetos! Você implementará um **gerador de relatórios** que recebe como entrada arquivos com dados de um estoque e gera, como saída, um relatório acerca destes dados.

  Esses dados de estoque poderão ser obtidos de diversas fontes:

  - Através da importação de um arquivo `CSV`;

  - Através da importação de um arquivo `JSON`;

  - Através da importação de um arquivo `XML`.

  Além disso, o relatório final possuirá duas versões: **simples** e **completa**.

  <strong>🚵 Habilidades a serem trabalhadas:</strong>
 

  <ul>
    <li>Aplicar conceitos de Orientação a Objetos em Python;</li>
    <li>Aplicar padrões de projeto;</li>
    <li>Leitura e escrita de arquivos (XML, CSV, JSON).</li>
  </ul>
</details>


<details>
  <summary><strong>🧱 Estrutura do Projeto</strong></summary><br />
  Este repositório já contém um template com a estrutura de diretórios e arquivos, tanto de código quanto de teste criados. Veja abaixo:

  ```
  Legenda:
  🔸Arquivos que não podem ser alterados
  🔹Arquivos a serem alterados para realizar os requisitos.
  .
  ├── inventory_report
  │   ├── data
  │   │   ├── 🔸inventory.csv
  │   │   ├── 🔸inventory.json
  │   │   └── 🔸inventory.xml
  │   ├── importer
  │   │   ├── 🔹csv_importer.py
  │   │   ├── 🔹importer.py
  │   │   ├── 🔹json_importer.py
  │   │   └── 🔹xml_importer.py
  │   ├── inventory
  │   │   ├── 🔹inventory_iterator.py
  │   │   ├── 🔹inventory_refactor.py
  │   │   └── 🔹inventory.py
  │   │   └── 🔸product.py
  │   ├── reports
  │   │   ├── 🔸colored_report.py
  │   │   ├── 🔹complete_report.py
  │   │   └── 🔹simple_report.py
  │   └── 🔹main.py
  └── tests
  │   ├── factories
  │   │   ├── 🔸__init__.py
  │   │   └── 🔸product_factory.py
  │   ├── product
  │   │   ├── 🔸__init__.py
  │   │   ├── 🔸conftest.py
  │   │   ├── 🔸mocks.py
  │   │   └── 🔹test_product.py
  │   ├── product_report
  │   │   ├── 🔸__init__.py
  │   │   ├── 🔸conftest.py
  │   │   ├── 🔸mocks.py
  │   │   └── 🔹test_product_report.py
  │   ├── report_decorator
  │   │   ├── 🔸__init__.py
  │   │   ├── 🔸conftest.py
  │   │   ├── 🔸mocks.py
  │   │   └── 🔹test_report_decorator.py
  │   ├── 🔸__init__.py
  │   ├── 🔸marker.py
  │   ├── 🔸test_complete_report.py
  │   ├── 🔸test_importer.py
  │   ├── 🔸test_inventory_refactor.py
  │   ├── 🔸test_inventory.py
  │   ├── 🔸test_main.py
  │   └── 🔸test_simple_report.py
  ├── 🔹dev-requirements.txt
  ├── 🔸docker-compose.yml
  ├── 🔸Dockerfile
  ├── 🔸pyproject.toml
  ├── 🔸README.md
  ├── 🔸requirements.txt
  ├── 🔸setup.cfg
  ├── 🔸setup.py
  └── 🔸trybe.yml
  ```

  Apesar do projeto já possuir uma **estrutura base**, você perceberá que possui arquivos vazios, ou seja, neles você quem deve implementar as classes. Novos arquivos e funções podem ser criados conforme a necessidade da sua implementação, porém não remova arquivos já existentes.

</details>

<details>
  <summary><strong>🎛 Linter</strong></summary><br />

  Para garantir a qualidade do código, vamos utilizar neste projeto o linter `Flake8`.
  Assim o código estará alinhado com as boas práticas de desenvolvimento, sendo mais legível
  e de fácil manutenção! Para rodá-lo localmente no projeto, execute o comandos abaixo:

  ```bash
  python3 -m flake8
  ```

  ⚠️ **PULL REQUESTS COM ISSUES DE LINTER NÃO SERÃO AVALIADAS.
  ATENTE-SE PARA RESOLVÊ-LAS ANTES DE FINALIZAR O DESENVOLVIMENTO!** ⚠️
</details>

<details>
  <summary><strong>🏕️ Ambiente Virtual</strong></summary><br />
  O Python oferece um recurso chamado de ambiente virtual, onde permite sua máquina rodar sem conflitos, diferentes tipos de projetos com diferentes versões de bibliotecas.

  1. **criar o ambiente virtual**

  ```bash
  $ python3 -m venv .venv
  ```

  2. **ativar o ambiente virtual**

  ```bash
  $ source .venv/bin/activate
  ```

  3. **instalar as dependências no ambiente virtual**

  ```bash
  $ python3 -m pip install -r dev-requirements.txt
  ```

  Com o seu ambiente virtual ativo, as dependências serão instaladas neste ambiente.
  Quando precisar desativar o ambiente virtual, execute o comando "deactivate". Lembre-se de ativar novamente quando voltar a trabalhar no projeto.

  O arquivo `dev-requirements.txt` contém todas as dependências que serão utilizadas no projeto, ele está agindo como se fosse um `package.json` de um projeto `Node.js`.
</details>


<details>
  <summary><strong>🗃️ Arquivos com os dados de entrada</strong></summary><br />
  Três formatos de importação estão disponíveis no diretório <code>data</code> dentro do diretório <code>inventory_report</code>. Confira o exemplo de formato eles:
  
  <strong>Arquivos CSV</strong>
  Os arquivos **CSV** são separados por vírgula, como no exemplo abaixo:

```CSV
id,nome_do_produto,nome_da_empresa,data_de_fabricacao,data_de_validade,numero_de_serie,instrucoes_de_armazenamento
1,cadeira,Target Corporation,2021-02-18,2025-09-17,CR25,empilhadas
2,mesa,"Galena Madeira, Inc.",2022-12-06,2026-12-25,FR29,desmontadas
3,abajur,Keen Iluminação,2019-12-22,2025-11-07,CZ09,em caixas
```

<strong>Arquivos JSON</strong>
Os arquivos JSON seguem o seguinte modelo:

```json
[
  {
    "id":1,
    "nome_do_produto":"Borracha",
    "nome_da_empresa":"Papelaria Solar",
    "data_de_fabricacao":"2021-07-04",
    "data_de_validade":"2029-02-09",
    "numero_de_serie":"FR48",
    "instrucoes_de_armazenamento":"Ao abrigo de luz solar"
  }
]
```

<strong>Arquivos XML</strong>
Os arquivos **XML** seguem o seguinte modelo:

```xml
<?xml version='1.0' encoding='UTF-8'?>
<dataset>
  <record>
    <id>1</id>
    <nome_do_produto>Microfone</nome_do_produto>
    <nome_da_empresa>Tecno Uau LTDA</nome_da_empresa>
    <data_de_fabricacao>2021-10-27</data_de_fabricacao>
    <data_de_validade>2032-08-31</data_de_validade>
    <numero_de_serie>MT08</numero_de_serie>
    <instrucoes_de_armazenamento>Longe de fonte de calor</instrucoes_de_armazenamento>
  </record>
</dataset>
```
</details>


---

# Requisitos obrigatórios

## 1 - Testar o construtor/inicializador do objeto Produto
> **Crie o teste em:** tests/product/test_product.py


Ao analisar o código do projeto, você encontrará a classe do objeto produto já implementada neste arquivo: `inventory_report/inventory/product.py`, a classe **Product**.

Para termos confiança em continuar as implementações, precisamos que você implemente o teste, que certifique que o método `__init__` da classe Product esta funcionando corretamente.

O nome deste teste deve ser `test_cria_produto`, ele deve verificar o correto preenchimento dos seguintes atributos:
  - id (int)
  - nome_da_empresa (string)
  - nome_do_produto (string)
  - data_de_fabricacao (string)
  - data_de_validade (string)
  - numero_de_serie (string)
  - instrucoes_de_armazenamento (string)


## 2 - Gerar a versão simplificada do relatório

> **Crie a classe em:** inventory_report/reports/simple_report.py

O relatório deve ser gerado através de um método estático ou de classe chamado `generate` escrito dentro da classe `SimpleReport`.

- Ao rodar os testes localmente, você terá um teste para cada validação de cada informação
- Deve ser possível executar o método `generate` sem instanciar um objeto de `SimpleReport`
- O método deve receber um parâmetro que representa uma `list` (estrutura de dados), onde cada posição contém um `dict`(estrutura de dados).

Exemplo de formato de entrada

```json
   [
     {
       "id": 1,
       "nome_do_produto": "CADEIRA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar em local fresco"
     }
   ]
```

- O método deverá retornar uma `string` de saída com o seguinte formato:
   ```bash
   Data de fabricação mais antiga: YYYY-MM-DD
   Data de validade mais próxima: YYYY-MM-DD
   Empresa com mais produtos: NOME DA EMPRESA
   ```
- A data de validade mais próxima, somente considera itens que ainda não venceram.


## 3 - Gerar a versão completa do relatório

> **Crie em:** inventory_report/reports/complete_report.py

O relatório deve ser gerado através de um método `generate` para a classe `CompleteReport`.
Ele deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá retornar uma string formatada como um relatório.

- A classe `CompleteReport` deve herdar da classe `SimpleReport` e sobrescrever o método `generate`, de modo a especializar seu comportamento.

- Deve ser possível executar o método `generate` sem instanciar um objeto de `CompleteReport`
  
- O método deve receber de parâmetro uma lista de dicionários no seguinte **formato**:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "MESA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-05-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
     }
   ]
   ```

- O método deverá retornar uma saída com o seguinte formato:

```bash
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
Produtos estocados por empresa:
- Physicians Total Care, Inc.: QUANTIDADE
- Newton Laboratories, Inc.: QUANTIDADE
- Forces of Nature: QUANTIDADE
```


## 4 - Gere os relatórios através de um arquivo CSV
> **Crie em:** inventory_report/inventory/inventory.py

A importação do arquivo CSV deve ser realizada através do método `import_data` que você deve criar em uma classe chamada `Inventory`.
    
O método deve ser estático ou de classe, ou seja, deve ser possível chamá-lo sem instanciar um objeto da classe.

O método receberá como primeiro parâmetro uma string como caminho para o arquivo `CSV` e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:
 - `"simples"`
 - `"completo"`

De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).


## 5 - Gere os relatórios através de um arquivo JSON
> **Incremente em:** `inventory_report/inventory/inventory.py`. 

> 📌 Utilize o mesmo método do requisito anterior.

Altere o método `import_data` para que ele também seja capaz de carregar arquivos `JSON`.
    
Como no requisito anterior, o método ainda receberá como primeiro parâmetro uma string como caminho para o arquivo, e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:
 - `"simples"`
 - `"completo"`

De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).


## 6 - Gere os relatórios através de um arquivo XML
> **Incremente em:** `inventory_report/inventory/inventory.py`. 

> 📌 Utilize o mesmo método do requisito anterior.
    
Altere o método `import_data` para que ele também seja capaz de carregar arquivos `XML`.
    
Como no requisito anterior, o método ainda receberá como primeiro parâmetro uma string como caminho para o arquivo, e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:
 - `"simples"`
 - `"completo"`

De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).


## 7 - Organizar o código de importação com o padrão Strategy
> **Crie em:** inventory_report/importer/importer.py

Como pôde observar até aqui, o método `import_data` está com muitas responsabilidades, e, com o intuito de resolver isso, podemos dividir a sua complexidade para cada formato de arquivo.

O padrão de projeto `Strategy` nos ajuda a isolar cada estratégia em um objeto, e por meio de uma Interface podemos padronizar a assinatura dos métodos, garantindo que todas elas possuam o comportamento similar.

- Ao rodar os testes localmente, você terá um teste para cada validação de cada informação
- Crie uma classe abstrata `Importer` para ser a interface da estratégia
- A Interface será uma classe abstrata `Importer` terá três classes de estratégias herdeiras: `CsvImporter`, `JsonImporter` e `XmlImporter`.
- Crie as classes nos respectivos arquivos:
  > inventory_report/importer/csv_importer.py
  > inventory_report/importer/json_importer.py
  > inventory_report/importer/xml_importer.py

- A classe abstrata deve definir a assinatura do método `import_data` a ser implementado por cada classe herdeira. Esse método deve ser estático ou de classe, e deve receber como parâmetro o nome do arquivo a ser importado.

- O método `import_data` definido por cada classe herdeira deve lançar uma exceção do tipo `ValueError` caso a extensão do arquivo passado por parâmetro seja inválida. Por exemplo, quando se passa um caminho de um arquivo com extensão `.csv` para o `JsonImporter`. A mensagem de erro da exceção deve ser _"Arquivo inválido"_.

- O método deverá ler os dados do arquivo passado e retorná-los estruturados em uma lista de dicionários conforme exemplo abaixo:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "Cafe",
       "nome_da_empresa": "Cafes Nature",
       "data_de_fabricacao": "2020-07-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "instrucao"
     }
   ]
   ```


## 8 - Testar o relatório individual do produto
> **Crie o teste em:** tests/product_report/test_product_report.py

Boa novidade, o primeiro relatório já implementamos neste arquivo `inventory_report/inventory/product.py`. Formulamos uma frase construída com as informações do produto, que será muito útil para etiquetarmos o estoque.

Para desenvolver este relatório, utilizamos o recurso `__repr__` do Python, que permite alterar a representatividade do objeto, para que sempre que usarmos um print nele, no lugar de endereço de memória, teremos uma String personalizada.

**Dica:** A reimplementação do `__repr__` não faz o objeto retornar exatamente uma `string`, fazer um `cast` para `string`, pode te ajudar.

Exemplo da frase:
> O produto `farinha` fabricado em `01-05-2021` por `Farinini` com validade até `02-06-2023` precisa ser armazenado `ao abrigo de luz`.

Agora para mantermos uma boa cobertura de testes, precisamos que você implemente o teste.

O nome deste teste deve ser `test_relatorio_produto`, ele deve instanciar um objeto `Product` e verificar se acessá-lo a frase de retorno esta correta.


## 9 - Testar a geração de uma versão do relatório em cores
> **Crie o teste em:** tests/report_decorator/test_report_decorator.py

Uma versão deste relatório será exibida em letreiros em Led, estes letreiros são coloridos, para isso, já implementamos o método responsável por retornar este relatório em cores.

> Implementamos em : inventory_report/reports/colored_report.py

Em vez de criarmos uma classe que herda os relatórios originais, utilizamos o padrão `Decorator` para receber o tipo do relatório por composição (`SimpleReport` ou `CompleteReport`) e, assim, colorir o retorno do método `generate`, que recebe uma lista de produtos e retorna o relatório já colorido.

Para termos confiança que as cores sairão corretamente, precisamos que você implemente o teste, que certifique que o método **generate**  de **ColoredReport** funciona corretamente.

Para que o Python consiga colorir as strings, é preciso que a string contenha o início do código da cor, e o reset da cor.

📌 Execute este print teste em um terminal interativo `python3 -i`. O resultado das cores podem não ser exatos, por isso, atente-se aos códigos deste exemplo:

```python
print("\033[36mAzul\033[0m \033[32mVerde\033[0m \033[31mVermelho\033[0m")
```

O nome deste teste deve ser `test_decorar_relatorio`, ele deve verificar se o relatório está devidamente colorido. Representamos abaixo como deve ser a disposição das cores:

<span style="color: green;">🟩Data de fabricação mais antiga:🟩</span> <span style="color: blue;">🟦10-05-2022🟦</span>

<span style="color: green;">🟩Data de validade mais próxima:🟩</span> <span style="color: blue;">🟦14-06-2021🟦</span>

<span style="color: green;">🟩Empresa com mais produtos:🟩</span> <span style="color: red;">🟥Farinini🟥</span>

  
# Requisitos bônus

## 10 - Criar uma classe `InventoryIterator`

> **Crie em:** inventory_report/inventory/inventory_iterator.py
    
O estoque será mostrado por painéis de led. Para não sobrecarregarmos a memória destes painéis, queremos poder iterar pelos itens do estoque, um item por vez. Para isso, precisamos primeiro refatorar a forma com que importamos os dados, e então aplicar o Padrão Iterator.
 
- A classe `Inventory` deverá ser refatorada (copiada) em outro arquivo chamado `inventory_report/inventory/inventory_refactor.py`. Nesse arquivo você irá refatorar a classe `Inventory` chamando-a de `InventoryRefactor`.

- A classe `InventoryRefactor` deve utilizar as classes definidas no requisito 8 para lidar com a lógica de importação, via **composição** no método `import_data`.

- A classe `InventoryRefactor` deve receber por seu construtor a classe que será utilizada para lidar com a lógica de importação e armazenar em um atributo chamado `importer`.
  
- A classe `InventoryRefactor` deve ter um método *de instância* que recebe um caminho para o arquivo a ser importado, e carrega seus dados.

- Ao importar os dados, os mesmos devem ser armazenados na instância, em adição aos itens já presentes naquela instância. O atributo de `InventoryRefactor` que armazena esses dados deve se chamar `data`.

- Os atributos e os métodos devem ser públicos.

- A classe `InventoryIterator` deverá implementar a interface de um iterator (`Iterator`) com o método `__next__`. Além disso, a classe `InventoryRefactor` deve implementar o método `__iter__`, que retornará este iterador.
    
- As classes `InventoryIterator` e `InventoryRefactor` devem implementar corretamente a interface do padrão de projeto **Iterator**, de modo que seja possível iterar sobre os itens em estoque.
    

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>

```python
iterator = iter(inventory)
first_item = next(iterator)
```
</details>


## 11 - Preencha a função `main` no módulo `inventory_report/main.py`

Essa função deve, ao receber pela linha de comando o caminho de um arquivo e o tipo de relatório, devolver o relatório correto.

- Deverá ser usado a classe `InventoryRefactor` para recuperar os dados e gerar o relatório.

- Ao chamar o comando no formato abaixo pelo terminal, deve ser impresso na tela o devido relatório no formato da saída dos requisitos `3` e `4`: 

```bash
inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>
```

- Caso a chamada tenha menos de três argumentos (o nome `inventory_report` é considerado o primeiro argumento), exiba a mensagem de erro "Verifique os argumentos" na `stderr`.
    
**Dicas:**
  - Se o comando não encontrar o pacote `inventory_report`, basta executar `pip install .` na raiz do projeto.

  - Você pode utilizar o `sys.argv` para receber a entrada de dados da pessoa usuária.
    
  - Ao utilizar algo do módulo `sys`, faça a importação com `import sys` e utilize `sys.xxxx` (onde xxxx é o que você quer utilizar). Não faça `from sys import xxxx`, pois isso pode fazer com que os testes não passem.
    
  - Tome a precaução de não deixar um `print()` em seu código, pois ele irá conflitar com os testes.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary> No ambiente virtual onde seu projeto foi configurado, instale o próprio projeto com o comando
  <code>pip install .</code>
  Agora execute o projeto com:
  <code>inventory_report parametro_1 parametro_2</code>
  exemplo:
  <code>inventory_report inventory_report/data/inventory.csv simples</code>
  Desta forma você conseguirá interagir gerar o relatório com o comando.
</details>
