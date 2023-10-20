def merge(lista1, lista2):
    i = j = 0
    aux = []
    
    while ((i < len(lista1)) and (j < len(lista2))):
        if (lista1[i] < lista2[j]):
            aux.append(lista1[i])
            i += 1
        else:
            aux.append(lista2[j])
            j += 1
    
    while (i < len(lista1)):
        aux.append(lista1[i])
        i += 1
        
    while (j < len(lista2)):
        aux.append(lista2[j])
        j += 1
    
    return aux

def merge_sort(lista, inicio, fim):
    if ((fim - inicio) > 1):
        meio = (inicio + fim) // 2
        
        lista = merge_sort(lista, inicio, meio)
        lista = merge_sort(lista, meio, fim)
        
        lista1 = lista[inicio : meio]
        lista2 = lista[meio : fim]
        
        lista[inicio : fim] = merge(lista1, lista2)
    
    return lista

def main():
    lista = [153, 120, 148, 213, 93, 120, 114, 193, 201]
    n = len(lista)
    listaOrdenada = merge_sort(lista, 0, n)
    print(listaOrdenada)
    
    return

main()
    