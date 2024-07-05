import random

def sortear_nomes(nomes):
    """
    Sorteia metade dos nomes da lista fornecida, excluindo o nome 'Ricardo'.
    Se o número de nomes for ímpar, retorna mais da metade.

    Args:
    nomes (list): Lista de nomes.

    Returns:
    list: Lista com metade dos nomes sorteados, ou mais da metade se o número de nomes for ímpar.
    """
    if not nomes:
        return []
    
    # Remove o nome 'Ricardo' da lista, se presente
    nomes = [nome for nome in nomes if nome.lower() != "ricardo"]
    
    # Embaralha a lista de nomes
    random.shuffle(nomes)
    
    # Calcula a metade da lista, arredondando para cima se o número de nomes for ímpar
    metade = len(nomes) // 2
    if len(nomes) % 2 != 0:
        metade += 1
    
    # Retorna a primeira metade da lista embaralhada
    return nomes[:metade]
