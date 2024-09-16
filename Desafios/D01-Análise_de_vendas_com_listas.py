def obter_entrada_vendas():
    # Solicita a entrada do usuário em uma única linha
    entrada = input()

    # TODO: Converta a entrada em uma lista de inteiros:
    lista_vendas = list(map(int, entrada.split(',')))

    # Validei com o método isinstance percorrendo com um for se os valores haviam sido convertido em int:
    all(isinstance(i, int) for i in lista_vendas)

    # Retonei com valores ja convertidos em int:
    return lista_vendas

# vendas = obter_entrada_vendas()


def analise_vendas(vendas):
    # TODO: Calcule o total de vendas e realize a média mensal:
    total_vendas = sum(vendas)

    # Calcula a media de todos os produtos contidos na lista_vendas:
    media_vendas = total_vendas / len(vendas)

    # Retorna o total_vendas e media_vendas convertidos em int:
    return f"{total_vendas}, {media_vendas:.2f}"

# analise_vendas(vendas)



vendas = obter_entrada_vendas()
print(analise_vendas(vendas))