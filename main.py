import os
from Algoritmos import branch_and_bound, codificacao_de_Huffman, fractional_knapsack, mochila_booleana, subsequencia_mais_longa


def print_menu():
    print("\n\nEsse projeto implementa soluções para os seguintes problemas:\n"
          "1. Problema de Associação de Tarefas (Assignment Problem)\n"
          "2. Codificação de Huffman para compressão de um texto\n"
          "3. Problema da Mochila Fracionária (Fractional Knapsack Problem)\n"
          "4. Problema da Mochila Booleana (Knapsack Problem)\n"
          "5. Problema da Subsequência Comum Máxima (Longest Common Subsequence)\n"
          "0. Sair")
    print("Digite o número do problema que deseja resolver ou '0' para encerrar o programa.")

def main():
    while True:
        print_menu()
        escolha = input("Escolha: ")

        if escolha == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            branch_and_bound.main_B_And_B()            
        elif escolha == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            codificacao_de_Huffman.main_huffman()
        elif escolha == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            fractional_knapsack.main_knapsack()            
        elif escolha == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            mochila_booleana.main()
        elif escolha == "5":
            os.system('cls' if os.name == 'nt' else 'clear')
            subsequencia_mais_longa.main()
        elif escolha == "0":
            os.system('cls' if os.name == 'nt' else 'clear')
            print ("Saindo...\n\n")
            break
        else:
            print("Escolha inválida. Tente novamente.")
            print_menu()

if __name__ == "__main__":
    main()
