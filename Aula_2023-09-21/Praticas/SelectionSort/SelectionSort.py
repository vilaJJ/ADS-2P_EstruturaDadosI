# • Função que retorna o índice do menor elemento de uma lista (formado por n números inteiros) a partir de uma posição inicial dada:
def indiceMenor(lista, inicio):
    minimo = inicio
    for i in range(inicio + 1, len(lista)):
        if(lista[minimo] > lista[i]):
            minimo = i
    return minimo

# • Usando a função auxiliar indiceMenor para implementar o Selection Sort da seguinte forma:
def selectionSort(lista):
    for i in range(len(lista) - 1):
        minimo = indiceMenor(lista, i)
        (lista[i], lista[minimo]) = (lista[minimo], lista[i])
    return lista

lista = [17, 5, 2005, 3, 1, 2004, 23, 6]

print(selectionSort(lista))