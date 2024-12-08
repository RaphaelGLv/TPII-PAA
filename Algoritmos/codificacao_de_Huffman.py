import heapq
from collections import Counter
class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        """
        Representa um nó da árvore de Huffman.
        
        Args:
            freq (int): Frequência do símbolo.
            symbol (str): Símbolo (caractere).
            left (Node, opcional): Nó filho à esquerda.
            right (Node, opcional): Nó filho à direita.
        """
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right
        self.huff = ''  # Direção no código (0 ou 1)

    def __lt__(self, other):
        return self.freq < other.freq


def criar_nos(chars, freq):
    """
    Cria uma lista de nós a partir dos caracteres e suas frequências.

    Args:
        chars (list): Lista de caracteres.
        freq (list): Lista de frequências correspondentes.

    Returns:
        list: Nós para construção da árvore.
    """
    return [Node(freq[i], chars[i]) for i in range(len(chars))]


def construir_arvore(nodes):
    """
    Constrói a árvore de Huffman a partir dos nós.

    Args:
        nodes (list): Lista de nós (min-heap).

    Returns:
        Node: Raiz da árvore de Huffman.
    """
    heapq.heapify(nodes)

    while len(nodes) > 1:
        # Remove os dois nós com menor frequência
        left = heapq.heappop(nodes)
        right = heapq.heappop(nodes)

        # Atribui direções aos nós
        left.huff = 0
        right.huff = 1

        # Cria um novo nó pai combinando os dois
        new_node = Node(left.freq + right.freq, left.symbol + right.symbol, left, right)
        heapq.heappush(nodes, new_node)

    return nodes[0]  # Raiz da árvore


def exibir_codigos_huffman(node, val='', codigos=None):
    """
    Gera e exibe os códigos de Huffman para cada símbolo.

    Args:
        node (Node): Raiz da árvore de Huffman.
        val (str, opcional): Código de Huffman acumulado.
        codigos (dict, opcional): Dicionário para armazenar os códigos.

    Returns:
        dict: Dicionário com os códigos de Huffman.
    """
    if codigos is None:
        codigos = {}

    new_val = val + str(node.huff)

    if node.left:
        exibir_codigos_huffman(node.left, new_val, codigos)
    if node.right:
        exibir_codigos_huffman(node.right, new_val, codigos)

    if not node.left and not node.right:
        codigos[node.symbol] = new_val
        print(f"{node.symbol} -> {new_val}")

    return codigos


def executar_huffman(chars, freq):
    """
    Executa o algoritmo de Huffman com os dados fornecidos.

    Args:
        chars (list): Lista de caracteres.
        freq (list): Lista de frequências correspondentes.
    """
    print("\nConstruindo a árvore de Huffman...")
    nodes = criar_nos(chars, freq)
    raiz = construir_arvore(nodes)

    print("\nCódigos de Huffman gerados:")
    exibir_codigos_huffman(raiz)


def calcular_frequencias(texto):
    """
    Calcula a frequência de cada caractere em uma string.

    Args:
        texto (str): A string de entrada para calcular frequências.

    Returns:
        tuple: Uma tupla contendo:
            - chars (list): Lista de caracteres únicos.
            - freq (list): Lista de frequências correspondentes.
    """
    texto = texto.replace(" ", "")  #Remove espaços da string

    # Usa Counter para contar a frequencia dos caracteres
    contador = Counter(texto)
    
    # Separa os caracteres e suas frequências
    chars = list(contador.keys())
    freq = list(contador.values())
    
    return chars, freq

# Exemplo de uso
texto = "huffman algorithm example"
chars, freq = calcular_frequencias(texto.replace(" ", ""))  # Remove espaços para não contá-los

def aux_uso(texto):
    print(f'Frase utilizada: "{texto}"')
    chars, freq = calcular_frequencias(texto)
    print("Caracteres:", chars)
    print("Frequências:", freq)
    executar_huffman(chars, freq)



def main_huffman():
    """
    Menu principal para execução do algoritmo de Huffman.
    """
    while True:
        print("\nMenu Huffman:")
        print("1. Usar dados pré-definidos")
        print("2. Inserir dados manualmente")
        print("3. Sair")

        opcao = input("Escolha uma opção (1, 2 ou 3): ")

        if opcao == "1":
            # Dados pré-definidos
            texto = "exemplo de uso da codificacao de Huffman"
            aux_uso(texto)

        elif opcao == "2":
            # Inserir frase manualmente
            texto = input("Digite uma frase para calcular as frequências: ")
            aux_uso(texto)
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")



