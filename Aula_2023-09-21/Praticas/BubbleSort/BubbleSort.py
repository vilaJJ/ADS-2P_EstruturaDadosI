# • Note que as comparações na primeira iteração ocorrem até a última posição da lista.
# • Na segunda iteração, elas ocorrem até a penúltima posição.
# • E assim sucessivamente...

def bubbleSortPy(lista):
    for i in range(len(lista) - 1, 0, -1):
        for j in range(i):
            if(lista[j] > lista[j + 1]):
                (lista[j], lista[j + 1]) = (lista[j + 1], lista[j])
    return lista

def bubbleSortDefault(lista):
    for i in range(len(lista) - 1, 0, -1):
        for j in range(i):
            if(lista[j] > lista[j + 1]):
                aux = lista[i]
                lista[i] = lista[j]
                lista[j] = aux
    return lista

lista1 = [404, 502, 200, 69, 420]

print(bubbleSortPy(lista1))
print(bubbleSortDefault(lista1))