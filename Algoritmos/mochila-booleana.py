class Item :
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

def gerar_itens_aleatorios(tamanho):
    from random import randint
    return [Item(randint(1, 10), randint(1, 10)) for _ in range(tamanho)]

def mochila_booleana(itens, capacidade):
    tamanho = len(itens)

    # Inicializa a tabela de resposta com zeros
    tabela_resposta = [[0] * (capacidade + 1) for _ in range(tamanho + 1)]
    
    # Percorre a tabela de resposta
    for i in range(1, tamanho + 1):
        for j in range(1, capacidade + 1):
            # Se o peso do item for menor ou igual a capacidade da mochila
            if itens[i - 1].peso <= j:
                # Pega o máximo entre o valor do item atual + o valor da mochila com o peso restante
                tabela_resposta[i][j] = max(tabela_resposta[i - 1][j], itens[i - 1].valor + tabela_resposta[i - 1][j - itens[i - 1].peso])
            else:
                # Se o peso do item for maior que a capacidade da mochila, pega o valor da linha anterior
                tabela_resposta[i][j] = tabela_resposta[i - 1][j]

    # Retorna o valor máximo que a mochila pode carregar
    return tabela_resposta[tamanho][capacidade]