def pesquisa_binaria(A, item):
    return pesquisa_binaria_recursiva(A, 0, len(A) - 1, item)

def pesquisa_binaria_recursiva(A, esquerda, direita, item):
    """Implementa pesquisa binária recursivamente."""
    # 1. Caso base: o elemento não está presente. 
    if direita < esquerda:
        return -1
    meio = (esquerda + direita) // 2
    # 2. Nosso palpite estava certo: o elemento está no meio do arranjo. 
    if A[meio] == item:
        return meio
    # 3. O palpite estava errado: atualizamos os limites e continuamos a busca. 
    elif item < A[meio]:
        return pesquisa_binaria_recursiva(A, esquerda, meio - 1, item)
    else: # item > A[meio]
        return pesquisa_binaria_recursiva(A, meio + 1, direita, item)

A = [0, 10, 20, 30, 40, 50, 60, 70]
print("Pesquisa com sucesso:", pesquisa_binaria(A, 20))
print("Pesquisa com sucesso:", pesquisa_binaria(A, 0))
print("Pesquisa com sucesso:", pesquisa_binaria(A, 70))
print("Pesquisa com sucesso:", pesquisa_binaria(A, 100))