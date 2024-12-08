class Item:
    """
    Classe que representa um item da mochila.

    Attributes:
        peso (int): O peso do item.
        valor (int): O valor do item.
        densidade (float): A densidade do item, calculada como o valor dividido pelo peso.
    """
    def __init__(self, peso, valor):
        """
        Inicializa os atributos do item.

        Args:
            peso (int): O peso do item.
            valor (int): O valor do item.
        """
        self.peso = peso
        self.valor = valor
        self.densidade = valor / peso  
    
    def __repr__(self): # para poder printar corretamente
        """
        Representação legível do item, exibindo seu peso e valor.

        Returns:
            str: Representação do item como uma string.
        """
        return f"Item(peso={self.peso}, valor={self.valor}, densidade={self.densidade:.2f})"


def fractional_knapsack(capacidade, itens):
    """
    Implementação do algoritmo de mochila fracionária.

    Args:
        capacidade (int): A capacidade total da mochila.
        itens (list): Lista de itens disponíveis para colocar na mochila, cada item é uma instância da classe Item.

    Returns:
        tuple: O valor total da mochila fracionária e a disposição dos itens na mochila (inteiros ou fracionados).
    """
    # Ordenação decrescente pela densidade
    itens.sort(key=lambda x: x.densidade, reverse=True)

    # Verifica se a capacidade é válida
    if capacidade <= 0:
        print("Capacidade inválida")
        return
    
    valor_total = 0
    mochila = []

    # Loop para adicionar itens ou frações de itens à mochila
    for item in itens:
        if capacidade == 0:
            break

        if item.peso <= capacidade: #itens inteiros
            capacidade -= item.peso
            valor_total += item.valor
            mochila.append((item.peso, item.valor, 1))  
        else:
            valor_total += item.valor * (capacidade / item.peso)
            mochila.append((capacidade, item.valor * (capacidade / item.peso), capacidade / item.peso))  #itens fracionados
            capacidade = 0

    return valor_total, mochila

def print_Mochila(mochila):
    """
    Exibe a disposição dos itens na mochila, informando se o item é inteiro ou fracionado.

    Args:
        mochila (list): Lista contendo a disposição dos itens na mochila.
    """
    print("\nDisposição dos itens na mochila:")
    for peso, valor, fracao in mochila:
        if fracao == 1:
            print(f"Item inteiro - Peso: {peso}, Valor: {valor}")
        else:
            print(f"Item fracionado - Peso: {peso}, Valor: {valor}, Fração: {fracao:.2f}")

def exibir_mochila(capacidade, itens):
    """
    Exibe o valor total da mochila fracionária e a disposição dos itens.

    Args:
        capacidade (int): A capacidade da mochila.
        itens (list): Lista de itens (instâncias da classe Item).
    """
    resultado, mochila = fractional_knapsack(capacidade, itens)
    print(f"\nValor total da mochila fracionária: {resultado}")
    print_Mochila(mochila)


def main_knapsack():
    """
    Menu principal para execução do algoritmo de mochila fracionária.
    Permite que o usuário escolha entre usar dados pré-definidos ou inserir dados manualmente.
    """
    while True:
        print("\nMenu Mochila Fracionária:")
        print("1. Usar dados pré-definidos")
        print("2. Inserir dados manualmente")
        print("3. Sair")

        opcao = input("Escolha uma opção (1, 2 ou 3): ")

        if opcao == "1":
            # Dados pré-definidos
            itens = [Item(40, 200), Item(20, 20), Item(11, 110)]
            capacidade = 50
            print(f"Capacidade da Mochila: {capacidade}")
            print("Itens na mochila:")
            for item in itens:
                print(f"Peso: {item.peso}, Valor: {item.valor}")


            exibir_mochila(capacidade, itens)

        elif opcao == "2":
            # Inserir dados manualmente
            try:
                capacidade = int(input("Digite a capacidade da mochila: "))
                n = int(input("Quantos itens você deseja adicionar? "))
                itens = []

                # Loop para coletar os dados dos itens
                for i in range(n):
                    peso = int(input(f"Digite o peso do item {i+1}: "))
                    valor = int(input(f"Digite o valor do item {i+1}: "))
                    itens.append(Item(peso, valor))

                exibir_mochila(capacidade, itens)

            except ValueError:
                print("Por favor, insira valores válidos.")

        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

