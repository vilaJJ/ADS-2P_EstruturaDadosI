# Função para somar uma lista de números
def somar_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + somar_lista(lista[1:])

# Executando função:
numeros = [10, 20, 30]
soma = somar_lista(numeros)
print(f'A soma dos números {numeros} é {soma}')