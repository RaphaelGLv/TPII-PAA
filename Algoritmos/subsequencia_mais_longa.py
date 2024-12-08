class CelulaResposta:
    def __init__(self, valor, direcao):
        self.valor = valor
        self.direcao = direcao

class LCS:
    @staticmethod
    def _gerar_tabela_resposta(seq1, seq2):
        tamanho_seq1 = len(seq1)
        tamanho_seq2 = len(seq2)
        
        # Inicializa a tabela de resposta com zeros
        tabela_resposta = [[0] * (tamanho_seq2 + 1) for _ in range(tamanho_seq1 + 1)]
        tabela_resposta[0] = [0] * (tamanho_seq2 + 1)

        # Percorre a tabela de resposta
        for i in range(1, tamanho_seq1 + 1):
            for j in range(1, tamanho_seq2 + 1):
                if seq1[i - 1] == seq2[j - 1]:
                    # Se os caracteres forem iguais, incrementa o valor da diagonal anterior
                    tabela_resposta[i][j] = tabela_resposta[i - 1][j - 1] + 1
                else:
                    # Caso contrário, pega o maior valor entre a celula superior e da esquerda
                    tabela_resposta[i][j] = max(tabela_resposta[i - 1][j], tabela_resposta[i][j - 1])

        # Retorna o comprimento da maior subsequência comum
        return tabela_resposta

    @staticmethod
    def obter_subsequencia_mais_longa(seq1, seq2):
        tabela_resposta = LCS._gerar_tabela_resposta(seq1, seq2)
        tamanho_seq1 = len(seq1)
        tamanho_seq2 = len(seq2)
        
        # Inicializa a subsequência mais longa
        subsequencia = []
        
        # Começa do canto inferior direito da tabela
        i, j = tamanho_seq1, tamanho_seq2
        
        while i > 0 and j > 0:
            if seq1[i - 1] == seq2[j - 1]:
                # Se os caracteres forem iguais, faz parte da subsequência mais longa
                subsequencia.append(seq1[i - 1])
                i -= 1
                j -= 1
            elif tabela_resposta[i - 1][j] >= tabela_resposta[i][j - 1]:
                # Move para cima se o valor da célula superior for maior ou igual
                i -= 1
            else:
                # Move para a esquerda se o valor da célula esquerda for maior
                j -= 1
        
        # A subsequência está em ordem reversa, então inverte antes de retornar
        subsequencia.reverse()
        return subsequencia