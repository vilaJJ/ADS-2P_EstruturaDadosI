def particionar(lista, inicio, fim):
    j = inicio
    
    for i in range(inicio + 1, fim):
        if lista[i] <= lista[inicio]:
            j += 1
            (lista[i], lista[j]) = (lista[j], lista[i])
    
    (lista[inicio], lista[j]) = (lista[j], lista[inicio])
    
    return j

def quick_sort(lista, inicio, fim):
    if(fim - inicio) > 1:
        pivo = particionar(lista, inicio, fim)
        
        quick_sort(lista, inicio, pivo)
        quick_sort(lista, pivo + 1, fim)

    return lista

def main():
    lista = [404, 200, 504, 522, 502, 201, 223, 401]
    lista_lenght = len(lista)
    
    lista_ordenada = quick_sort(lista, 0, lista_lenght)
    print(lista_ordenada)

main()