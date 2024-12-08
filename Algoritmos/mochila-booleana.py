import os

class Item :
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

    def __repr__(self):
        return f"{{ peso: {self.peso}, valor: {self.valor} }}"

    @staticmethod
    def gerar_itens_aleatorios(tamanho):
        from random import randint
        return [Item(randint(1, 10), randint(1, 10)) for _ in range(tamanho)]

class MochilaBooleana:
    @staticmethod
    def _gerar_tabela_resposta(itens, capacidade):
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
        return tabela_resposta

    @staticmethod
    def _extrair_itens_escolhidos(itens, capacidade, tabela_resposta):
        tamanho = len(itens)
        itens_escolhidos = []

        i, j = tamanho, capacidade
        while i > 0 and j > 0:
            if tabela_resposta[i][j] != tabela_resposta[i - 1][j]:
                itens_escolhidos.append(itens[i - 1])
                j -= itens[i - 1].peso
            i -= 1

        return itens_escolhidos

    @staticmethod
    def mochila_booleana(itens, capacidade):
        tabela_resposta = MochilaBooleana._gerar_tabela_resposta(itens, capacidade)
        valor_maximo = tabela_resposta[-1][-1]
        itens_escolhidos = MochilaBooleana._extrair_itens_escolhidos(itens, capacidade, tabela_resposta)
        return valor_maximo, itens_escolhidos

def main():
    print("Problema da Mochila Booleana\n")
    print("Para gerar itens aleatórios, digite '1'.")
    print("Para inserir manualmente, digite '2'.")

    escolha = input("Escolha: ")

    if escolha == '1':
        tamanho = int(input("Digite o número de itens a serem gerados: "))
        itens = Item.gerar_itens_aleatorios(tamanho)
    elif escolha == '2':
        tamanho = int(input("Digite o número de itens: "))
        itens = []
        for i in range(tamanho):
            peso = int(input(f"Digite o peso do item {i + 1}: "))
            valor = int(input(f"Digite o valor do item {i + 1}: "))
            itens.append(Item(peso, valor))
    else:
        print("Escolha inválida.")
        return
    
    capacidade = int(input("Digite a capacidade da mochila: "))
    valor_maximo, itens_escolhidos = MochilaBooleana.mochila_booleana(itens, capacidade)

    os.system('cls' if os.name == 'nt' else 'clear')

    print("\nItens disponíveis:")
    for i, item in enumerate(itens):
        print(f"{i + 1}: {item}")
    print("\nResultados:")
    print(f"O valor máximo que a mochila pode carregar é: {valor_maximo}")
    print("Itens escolhidos:")
    for item in itens_escolhidos:
        print(f"Peso: {item.peso}, Valor: {item.valor}")
