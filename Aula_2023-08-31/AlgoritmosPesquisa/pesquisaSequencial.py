def pesquisa_linear(arranjo, elemento_desejado):
    for i in range(len(arranjo)):
        if arranjo[i] == elemento_desejado:
            print(f"Elemento {elemento_desejado} está presente no arranjo.")
            return
    print(f"Elemento {elemento_desejado} não está presente no arranjo.")

def pesquisa_linear2(arranjo, elemento_desejado):
    for i in range(len(arranjo)):
        if arranjo[i] == elemento_desejado:
            return True
    return False


def pesquisa_linear3(arranjo, elemento_desejado):
    for i in range(len(arranjo)):
        if arranjo[i] == elemento_desejado:
            return i
    return -1


arranjo = [1,3,6,8,2,7,5,3,0,9,4]

# Pesquisa por elemento presente.
pesquisa_linear(arranjo, 0)

# Pesquisa por elemento ausente.
print(pesquisa_linear3(arranjo, 7))

# for e in arranjo: print(e+5)