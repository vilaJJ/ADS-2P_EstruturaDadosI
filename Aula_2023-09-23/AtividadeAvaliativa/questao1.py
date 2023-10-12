# Função para ordenação por bubble sort
def bubble_sort(arr):
    array = arr
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

# Função para ordenação por selection sort
def selection_sort(arr):
    for i in range(len(arr) - 1):
        minimo = indiceMenor(arr, i)
        (arr[i], arr[minimo]) = (arr[minimo], arr[i])
    return arr

# Função para ordenação por insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Função que retorna o índice do menor elemento de uma lista (formado por n números inteiros) a partir de uma posição inicial dada:
def indiceMenor(lista, inicio):
    minimo = inicio
    for i in range(inicio + 1, len(lista)):
        if(lista[minimo] > lista[i]):
            minimo = i
    return minimo

# Execuções
arr = [8, 20, 3, 2, 9]

print(bubble_sort(arr.copy()))
print(selection_sort(arr.copy()))
print(insertion_sort(arr.copy()))