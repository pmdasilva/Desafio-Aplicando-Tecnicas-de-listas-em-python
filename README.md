# Desafio-Aplicando-Tecnicas-de-listas-em-python
Desafio proposto pelo bootcamp, para melhoramento de habilidades tecnicas com python.


# Resolução do Exercicios - 001 - Aplicando Técnicas de Listas em Python. - Analise de vendas.

### Descrição
Você está trabalhando em um projeto de Power BI onde precisa analisar dados de vendas mensais de uma empresa. Em Power BI, os dados são frequentemente representados em tabelas, e você precisa calcular alguns indicadores básicos. Sua tarefa é calcular o total de vendas e a média mensal de vendas que serão usados para gerar relatórios e gráficos no Power BI, além de criar uma lista em Python para calcular o total de vendas e a sua média mensal.

### Detalhamento:
Na função obter_entrada_vendas() você deverá:

Utilizar o método split(',') para dividir a string de entrada em elementos separados por vírgula, criando assim uma lista de strings.

Aplique a função map(int, ...) para converter cada elemento dessa lista de strings em um inteiro.

Usar a função list() para converter o objeto map resultante em uma lista de inteiros.

Essa lista de inteiros representará os valores de vendas que serão utilizados para calcular o total e a média mensal de vendas em outra função.

### Entrada
Uma lista com 12 números inteiros, cada um representando o número de vendas realizadas em um mês do ano.

### Saída
Um único número inteiro representando o total de vendas e um número decimal representando a média mensal de vendas, separados por um espaço.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

### Entrada:
* 120, 150, 170, 130, 200, 250, 180, 220, 210, 160, 140, 190
* 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120
* 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60
### Saída:
* 2120, 176.67
* 780, 65.00
* 390, 32.50

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

![alt text](image.png)


# Resolução do Exercicios - 002 - Identificando os produtos mais vendidos.

### Descrição
Você está gerando um relatório de vendas em Power BI e deseja identificar quais produtos foram mais vendidos durante um dia específico. Os dados dos produtos vendidos são frequentemente armazenados em listas. Sua tarefa é usar uma lista em Python para contar a frequência de cada produto e determinar o produto mais vendido, que será usado para destacar produtos populares no relatório do Power BI.

### Detalhamento:
Encontre o produto com a maior contagem:

Itere sobre o dicionário contagem, que contém a contagem de cada produto.

Compare a contagem atual com a contagem máxima armazenada em max_count.

Se a contagem atual for maior que max_count, atualize max_count e defina max_produto como o produto atual.

Converter a entrada em uma lista de strings, removendo espaços extras:

Use o método split(',') para dividir a string de entrada em uma lista de strings, separando pelo caractere vírgula.

Utilize uma list comprehension para remover espaços em branco extras ao redor de cada string, usando o método strip().

### Entrada
Uma lista de strings onde cada string representa o nome de um produto vendido.

### Saída
A string com o nome do produto mais vendido. Se houver empate, retorne qualquer um dos produtos mais vendidos.

### Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

### Entrada
* Notebook, Mouse, Teclado, Mouse, Monitor, Mouse, Teclado
* Impressora, Teclado, Monitor, Monitor, Teclado, Impressora, Impressora
* Webcam, Webcam, Headset, Monitor, Headset, Headset

### Saída
* Mouse
* Impressora
* Headset

Atenção: É extremamente importante que as entradas e saídas sejam exatamente iguais às descritas na descrição do desafio de código.

![alt text](image-1.png)