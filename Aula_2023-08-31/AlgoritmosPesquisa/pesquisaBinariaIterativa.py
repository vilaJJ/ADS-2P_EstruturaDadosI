def pesquisa_binaria(A, item):
    """Implementa pesquisa binária iterativamente."""
    esquerda, direita = 0, len(A) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if A[meio] == item:
            return meio
        elif A[meio] > item:
            direita = meio - 1
        else: # A[meio] < item
            esquerda = meio + 1
    return -1

A = [0, 10, 20, 30, 40, 50, 60, 70]
print("Pesquisa com sucesso:", pesquisa_binaria(A, 20))
print("Pesquisa com sucesso:", pesquisa_binaria(A, 0))
print("Pesquisa com sucesso:", pesquisa_binaria(A, 70))
print("Pesquisa com sucesso:", pesquisa_binaria(A, 100))