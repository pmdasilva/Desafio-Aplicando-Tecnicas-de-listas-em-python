def encontrar_produto_mais_vendido(entrada):
    # Converter a entrada em uma lista de strings, removendo espaços extras
    produtos = [produto.strip() for produto in entrada.split(',')]

    # Dicionário para armazenar a contagem de cada produto
    contagem = {}

    # Iterar sobre os produtos para contar a frequência de cada um
    for produto in produtos:
        if produto in contagem:
            contagem[produto] += 1
        else:
            contagem[produto] = 1

    # Variáveis para armazenar o produto mais vendido e sua contagem
    max_produto = None
    max_count = 0

    # Iterar sobre o dicionário para encontrar o produto com a maior contagem
    for produto, qtd in contagem.items():
        if qtd > max_count:
            max_count = qtd
            max_produto = produto

    return max_produto

# Entrada do usuario:
entrada = input()
print(encontrar_produto_mais_vendido(entrada))  # Saída: Mouse