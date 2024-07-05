import random

def sortear_nomes(nomes):
    """
    Sorteia metade dos nomes da lista fornecida, excluindo o nome 'Ricardo'.
    Se o número de nomes for ímpar, retorna mais da metade.
    Se houver mais de 8 nomes, retorna até 4 nomes.

    Args:
    nomes (list): Lista de nomes.

    Returns:
    list: Lista com metade dos nomes sorteados, ou até 4 nomes se houver mais de 8 nomes.
    """
    if not nomes:
        return []
    
    # Remove o nome 'Ricardo' da lista, se presente
    nomes = [nome for nome in nomes if nome.lower() != "ricardo"]
    
    # Embaralha a lista de nomes
    random.shuffle(nomes)
    
    # Define a quantidade de nomes a serem sorteados
    if len(nomes) > 8:
        quantidade_sorteada = min(4, len(nomes))
    else:
        metade = len(nomes) // 2
        if len(nomes) % 2 != 0:
            metade += 1
        quantidade_sorteada = metade
    
    # Retorna a quantidade de nomes sorteada
    return nomes[:quantidade_sorteada]
