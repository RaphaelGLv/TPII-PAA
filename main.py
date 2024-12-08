from Algoritmos import codificacao_de_Huffman, mochila_booleana, subsequencia_mais_longa

def print_menu():
    print("Esse projeto implementa soluções para os seguintes problemas:\n"
          "1. Problema de Associação de Tarefas (Assignment Problem)\n"
          "2. Codificação de Huffman para compressão de um texto\n"
          "3. Problema da Mochila Fracionária (Fractional Knapsack Problem)\n"
          "4. Problema da Mochila Booleana (Knapsack Problem)\n"
          "5. Problema da Subsequência Comum Máxima (Longest Common Subsequence)\n"
          "0. Sair")
    print("Digite o número do problema que deseja resolver ou '0' para encerrar o programa.")

def main():
    print_menu()

    while True:
        escolha = input("Escolha: ")

        if escolha == "1":
            # assignment_problem.main()
            break;
        elif escolha == "2":
            codificacao_de_Huffman.main_huffman()
        elif escolha == "3":
            # fractional_knapsack.main()
            break;
        elif escolha == "4":
            mochila_booleana.main()
        elif escolha == "5":
            subsequencia_mais_longa.main()
        elif escolha == "0":
            break
        else:
            print("Escolha inválida. Tente novamente.")
            print_menu()