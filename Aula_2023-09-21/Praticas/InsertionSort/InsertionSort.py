# • Podemos criar uma função que, dados uma lista e um índice i, insere o elemento de índice i entre os elementos das posições 0 e i-1 (pré-ordenados), de forma que todos os elementos entre as posições 0 e i fiquem ordenados:
def insertionDefault(lista, i):
    aux = lista[i]
    j = i - 1
    while((j >= 0) and (lista[j] > aux)):
        lista[j + 1] = lista[j]
        j = j - 1
    lista[j + 1] = aux
    return lista
    
# • Em Python podemos implementar a função insertion de forma ainda mais simples, inserindo o elemento na posição desejada com um único comando.
def insertionPy(lista, i):
    j = i - 1
    while((j >= 0) and (lista[j] > lista[i])):
        j = j - 1
    lista[j + 1  : i + 1] = [lista[i]] + lista[j + 1 : i]
    return lista

def insertionSort(lista):
    for i in range(1, len(lista)):
        lista = insertionPy(lista, i)
    return lista

lista = [2004, 5, 23, 2005, 1, 17, 2023, 6, 3]
print(insertionSort(lista))