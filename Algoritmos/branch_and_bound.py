def criar_tabela(x):
    """
    Cria uma tabela (matriz) de x pessoas e y tarefas, com valores definidos pelo usuário.
    
    Args:
        x (int): Número de pessoas & Número de tarefas.
    
    Returns:
        list: Matriz representando os custos.
    """
    tabela = []
    # Loop para criar cada linha (pessoa) da tabela
    for i in range(x):
        linha = []
        # Loop para adicionar os custos de cada tarefa para a pessoa i
        for j in range(x):
            # Solicita ao usuário o valor para a célula correspondente (custo de atribuição)
            valor = float(input(f"Digite o valor para a pessoa {i+1}, tarefa {j+1}: "))
            linha.append(valor)
        tabela.append(linha)  # Adiciona a linha à tabela
    return tabela


def exibir_tabela(tabela):
    """
    Exibe a tabela de forma organizada, incluindo rótulos para pessoas e tarefas.
    
    Args:
        tabela (list): A matriz de custos a ser exibida.
    
    Returns:
        None
    """
    x = len(tabela)  # Número de pessoas
    y = len(tabela[0])  # Número de tarefas
    
    # Exibe o cabeçalho da tabela com os rótulos das tarefas
    print("\nTabela de custos:")
    print(" " * 10 + "\t".join(f"T{j+1}" for j in range(y)))
    
    # Exibe as linhas da tabela, com rótulos para as pessoas
    for i in range(x):
        print(f"P{i+1}".ljust(10) + "\t".join(f"{tabela[i][j]:.2f}" for j in range(y)))


def branch_and_bound_passo_a_passo(matriz, profundidade=0, tarefas_restantes=None, custo_atual=0, melhor_solucao=None, atribuicao_atual=None):
    """
    Implementa o algoritmo Branch and Bound para o problema de atribuição de tarefas, com o objetivo de minimizar o custo total, mostrando o processo passo a passo
    
    Args:
        matriz (list): Matriz de custos (pessoas x tarefas), onde cada valor representa o custo de atribuir a tarefa a uma pessoa.
        profundidade (int, opcional): O índice da pessoa a ser atribuída. Inicia em 0.
        tarefas_restantes (set, opcional): Conjunto de tarefas que ainda precisam ser atribuídas.
        custo_atual (int, opcional): Custo acumulado até o momento.
        melhor_solucao (dict, opcional): Dicionário com a melhor solução (custo e atribuições).
        atribuicao_atual (list, opcional): Lista com as atribuições de tarefas feitas até o momento.
    
    Returns:
        dict: Dicionário com o menor custo encontrado e as atribuições correspondentes.
    """
    # Inicializa as variáveis na primeira chamada
    if tarefas_restantes is None:
        tarefas_restantes = set(range(len(matriz[0])))  # Inicializa com todas as tarefas disponíveis
    if melhor_solucao is None:
        melhor_solucao = {"custo_minimo": float("inf"), "atribuicao": []}  # Inicializa o melhor custo com infinito
    if atribuicao_atual is None:
        atribuicao_atual = []  # Inicializa a lista de atribuições

    # Caso base: todas as pessoas foram atribuídas
    if profundidade == len(matriz):
        # Atualiza a melhor solução encontrada
        if custo_atual < melhor_solucao["custo_minimo"]:
            melhor_solucao["custo_minimo"] = custo_atual
            melhor_solucao["atribuicao"] = atribuicao_atual[:]
        
        # Exibe o progresso quando a solução é encontrada
        print(f"\nSolução encontrada com custo {custo_atual}:")
        for i, tarefa in enumerate(atribuicao_atual):
            print(f"P{i+1} -> Tarefa T{tarefa+1}")
        
        print("Retornando para a etapa anterior...\n")
        return melhor_solucao

    # Explora as tarefas restantes para a pessoa atual
    for tarefa in list(tarefas_restantes):
        # Calcula o custo parcial da atribuição
        custo_parcial = custo_atual + matriz[profundidade][tarefa]
        
        # Calcula o Lower Bound, uma estimativa do custo mínimo das tarefas restantes
        bound = custo_parcial + sum(
            min(matriz[p][t] for t in tarefas_restantes if t != tarefa)  # Estima o custo para as tarefas restantes
            for p in range(profundidade + 1, len(matriz))
        )

        # Exibe o progresso atual da análise (custo parcial e lower bound)
        print(f"\nAnalisando atribuição: P{profundidade+1} -> Tarefa T{tarefa+1}")
        print(f"Custo parcial: {custo_parcial}, Lower Bound estimado: {bound}")

        # Poda: se o custo parcial mais o Lower Bound excede o melhor custo encontrado, ignora este ramo
        if bound >= melhor_solucao["custo_minimo"]:
            print("Este ramo foi podado, pois o custo excede o custo mínimo atual.\n")
            continue

        # Realiza a atribuição temporária
        tarefas_restantes.remove(tarefa)
        atribuicao_atual.append(tarefa)

        # Chama recursivamente para a próxima pessoa
        melhor_solucao = branch_and_bound_passo_a_passo(
            matriz, profundidade + 1, tarefas_restantes, custo_parcial, melhor_solucao, atribuicao_atual
        )

        # Volta atrás (backtracking) e tenta outra atribuição
        tarefas_restantes.add(tarefa)
        atribuicao_atual.pop()

    return melhor_solucao

def branch_and_bound_direto(matriz, profundidade=0, tarefas_restantes=None, custo_atual=0, melhor_solucao=None, atribuicao_atual=None):
    """
    Implementa o algoritmo Branch and Bound para o problema de atribuição de tarefas, com o objetivo de minimizar o custo total.
    
    Args:
        matriz (list): Matriz de custos (pessoas x tarefas), onde cada valor representa o custo de atribuir a tarefa a uma pessoa.
        profundidade (int, opcional): O índice da pessoa a ser atribuída. Inicia em 0.
        tarefas_restantes (set, opcional): Conjunto de tarefas que ainda precisam ser atribuídas.
        custo_atual (int, opcional): Custo acumulado até o momento.
        melhor_solucao (dict, opcional): Dicionário com a melhor solução (custo e atribuições).
        atribuicao_atual (list, opcional): Lista com as atribuições de tarefas feitas até o momento.
    
    Returns:
        dict: Dicionário com o menor custo encontrado e as atribuições correspondentes.
    """
    if tarefas_restantes is None:
        tarefas_restantes = set(range(len(matriz[0])))
    if melhor_solucao is None:
        melhor_solucao = {"custo_minimo": float("inf"), "atribuicao": []}
    if atribuicao_atual is None:
        atribuicao_atual = []

    if profundidade == len(matriz):
        if custo_atual < melhor_solucao["custo_minimo"]:
            melhor_solucao["custo_minimo"] = custo_atual
            melhor_solucao["atribuicao"] = atribuicao_atual[:]
        return melhor_solucao

    for tarefa in list(tarefas_restantes):
        custo_parcial = custo_atual + matriz[profundidade][tarefa]
        bound = custo_parcial + sum(
            min(matriz[p][t] for t in tarefas_restantes if t != tarefa)
            for p in range(profundidade + 1, len(matriz))
        )

        # Poda: se o custo parcial mais o Lower Bound excede o melhor custo encontrado, ignora este ramo
        if bound >= melhor_solucao["custo_minimo"]:
            continue

        tarefas_restantes.remove(tarefa)
        atribuicao_atual.append(tarefa)

        melhor_solucao = branch_and_bound_direto(
            matriz, profundidade + 1, tarefas_restantes, custo_parcial, melhor_solucao, atribuicao_atual
        )

        tarefas_restantes.add(tarefa)
        atribuicao_atual.pop()

    return melhor_solucao


def exibir_solucao(solucao):
    """
    Exibe a melhor solução encontrada pelo algoritmo de Branch and Bound.
    
    Args:
        solucao (dict): Dicionário com o custo mínimo e a atribuição das tarefas.
    
    Returns:
        None
    """
    print("\nMelhor custo encontrado:", solucao["custo_minimo"])
    print("Atribuições:")
    # Exibe as atribuições de cada pessoa
    for i, tarefa in enumerate(solucao["atribuicao"]):
        print(f"Pessoa P{i+1} -> Tarefa T{tarefa+1}")


def main_B_And_B():
    # Menu principal
    while True:
        print("\nMenu Branch and Bound:")
        print("1. Usar uma matriz já pronta")
        print("2. Criar uma nova matriz")
        print("3. Sair")
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ")
        
        if opcao == "1":
            # Usar matriz pré-definida
            matriz = [
                [9, 2, 7, 8],
                [6, 4, 3, 7],
                [5, 8, 1, 8],
                [7, 6, 9, 4]
            ]
            print("\nMatriz de custos já definida:")
            exibir_tabela(matriz)
            menu_execucao(matriz)  # Chama o menu de execução com a matriz definida
        elif opcao == "2":
            # Criar nova matriz
            x = int(input("Digite o n da matriz: "))
            matriz = criar_tabela(x)
            print("\nMatriz de custos criada:")
            exibir_tabela(matriz)
            menu_execucao(matriz)  # Chama o menu de execução com a matriz criada
        elif opcao == "3":
            print("Saindo...")
            break  # Sai do programa
        else:
            print("Opção inválida. Tente novamente.")

def menu_execucao(matriz):
    # Menu de Execução do Branch and Bound
    while True:
        print("\nMenu de Execução do Branch and Bound:")
        print("1. Ver solução passo a passo")
        print("2. Ver apenas o resultado final")
        print("3. Voltar ao menu principal")
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ")
        
        if opcao == "1":
            # Chamando o Branch and Bound passo a passo
            print("\nIniciando a solução passo a passo:")
            solucao = branch_and_bound_passo_a_passo(matriz)
            exibir_solucao(solucao)
        elif opcao == "2":
            # Chamando o Branch and Bound apenas com o resultado final
            print("\nBuscando a melhor solução...")
            solucao = branch_and_bound_direto(matriz)
            exibir_solucao(solucao)
        elif opcao == "3":
            print("Voltando ao menu principal...")
            break  # Volta ao menu principal
        else:
            print("Opção inválida. Tente novamente.")

