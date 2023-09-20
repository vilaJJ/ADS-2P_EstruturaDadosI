# Define uma função chamada soma_lista que recebe uma lista de números como parâmetro
def soma_lista(lista):
    # Inicializa uma variável chamada soma com o valor zero
    soma = 0
    # Percorre cada elemento da lista usando um laço for
    for elemento in lista:
        # Adiciona o valor do elemento à variável soma
        soma = soma + elemento
    # Retorna o valor da variável soma como resultado da função
    return soma

# Cria uma lista de números chamada numeros
numeros = [1, 2, 3, 4, 5]
# Chama a função soma_lista passando a lista numeros como argumento e imprime o resultado
print(soma_lista(numeros))

# A função soma_lista usa a estrutura de dados lista, que é uma coleção ordenada e mutável de elementos1. 
# Uma lista pode armazenar qualquer tipo de dado, mas nesse caso estamos usando apenas números inteiros.
# A função percorre cada elemento da lista usando um laço for e acumula a soma dos valores em uma variável.
# No final, a função retorna o valor da soma como resultado