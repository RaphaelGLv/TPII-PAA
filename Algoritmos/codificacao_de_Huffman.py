import heapq
from collections import defaultdict

# Passo 1: Contagem das frequências dos caracteres
def calcular_frequencias(texto):
    frequencias = defaultdict(int)
    for char in texto:
        frequencias[char] += 1
    return frequencias

# Passo 2: Criação de uma árvore de Huffman
def construir_arvore_huffman(frequencias):
    # Criando uma lista de nós (heap) com as frequências
    heap = [[peso, [caractere, ""]] for caractere, peso in frequencias.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        # Pegando os dois nós com menores frequências
        baixo = heapq.heappop(heap)
        alto = heapq.heappop(heap)
        
        # Criando um novo nó com a soma das frequências
        for par in baixo[1:]:
            par[1] = '0' + par[1]
        for par in alto[1:]:
            par[1] = '1' + par[1]

        # Inserindo o novo nó de volta no heap
        nova_frequencia = baixo[0] + alto[0]
        heapq.heappush(heap, [nova_frequencia, baixo[1] + alto[1]])

    # O último nó contém a árvore completa
    # A árvore de Huffman está agora na forma de uma lista de listas [[peso, [caractere, código]]]
    # Precisamos extrair os pares (caractere, código) corretamente
    arvore_huffman = heap[0][1]
    return [(caractere, codigo) for caractere, codigo in arvore_huffman]

# Passo 3: Codificação do texto
def codificar_texto(texto, codigos):
    return ''.join(codigos[caractere] for caractere in texto)

# Passo 4: Função principal para executar a codificação
def huffman_compressao(texto):
    # Passo 1: Contar as frequências dos caracteres
    frequencias = calcular_frequencias(texto)

    # Passo 2: Construir a árvore de Huffman
    arvore_huffman = construir_arvore_huffman(frequencias)

    # Passo 3: Criar um dicionário de códigos a partir da árvore
    codigos = {caractere: codigo for caractere, codigo in arvore_huffman}

    # Passo 4: Codificar o texto
    texto_codificado = codificar_texto(texto, codigos)

    return texto_codificado, codigos

# Função main para testar o código
def main():
    texto = input("Digite o texto para compressão: ")
    
    # Passo 4: Executar a compressão usando Huffman
    texto_codificado, codigos = huffman_compressao(texto)
    
    # Exibir os resultados
    print("\nTexto original:", texto)
    print("Texto codificado:", texto_codificado)
    print("\nCódigos de Huffman:")
    for caractere, codigo in codigos.items():
        print(f"{caractere}: {codigo}")

if __name__ == "__main__":
    main()
