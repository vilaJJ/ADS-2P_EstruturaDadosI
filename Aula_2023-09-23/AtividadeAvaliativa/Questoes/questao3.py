import random
import time

# Criando um arranjo com 1000 posições e preenchendo-o com valores de 1 a 1000 de forma decrescente
# arr = [i for i in range(1000, 0, -1)]

# Criando um arranjo com 10000 posições e preenchendo-o com valores de 1 a 10000 de forma decrescente
# arr = [i for i in range(10000, 0, -1)]

# Criando um arranjo com 100000 posições e preenchendo-o com valores de 1 a 100000 de forma decrescente
arr = [i for i in range(100000, 0, -1)]

# Embaralhando o arranjo para garantir que está desordenado
random.shuffle(arr)

# Função para ordenação por bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

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

# Função que retorna o índice do menor elemento de uma lista (formado por n números inteiros) a partir de uma posição inicial dada:
def indiceMenor(lista, inicio):
    minimo = inicio
    for i in range(inicio + 1, len(lista)):
        if(lista[minimo] > lista[i]):
            minimo = i
    return minimo

# Medindo o tempo de execução para Bubble Sort
start_time = time.time()
bubble_sort(arr.copy())
bubble_sort_time = time.time() - start_time

# Embaralhando novamente para os próximos testes
random.shuffle(arr)

# Medindo o tempo de execução para Insertion Sort
start_time = time.time()
insertion_sort(arr.copy())
insertion_sort_time = time.time() - start_time

# Embaralhando novamente para os próximos testes
random.shuffle(arr)

# Medindo o tempo de execução para Selection Sort
start_time = time.time()
selection_sort(arr.copy())
selection_sort_time = time.time() - start_time

# Embaralhando novamente para os próximos testes
random.shuffle(arr)

# Imprimindo os tempos de execução
print("Tempo de execução para Bubble Sort: {:.6f} segundos".format(bubble_sort_time))
print("Tempo de execução para Selection Sort: {:.6f} segundos".format(selection_sort_time))
print("Tempo de execução para Insertion Sort: {:.6f} segundos".format(insertion_sort_time))