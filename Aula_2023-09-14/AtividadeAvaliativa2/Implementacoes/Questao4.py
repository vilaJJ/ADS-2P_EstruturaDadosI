from Helpers.ManipularArquivos import ManipularArquivos
from Helpers.Estudante import Estudante
import json

def pesquisaBinaria():
    id_estudante = int(input("Insira o ID do estudante: "))

    manipularArquivos = ManipularArquivos()
    dados_estudantes = manipularArquivos.open("../../LerArquivoBinario/dados_estudantes.txt")
    
    listaEstudantes = []

    for item in dados_estudantes:
        listaEstudantes.append(Estudante(json.loads(item)))

    esquerda, direita = 0, len(listaEstudantes) - 1
    
    while(esquerda <= direita):
        meio = (esquerda + direita) // 2
        estudante_while = listaEstudantes[meio]

        if(estudante_while.id == id_estudante):
            print("\nEstudante encontrado:\n")
            listaEstudantes[meio].apresentarInformacoes()
            return listaEstudantes[meio]
        elif(estudante_while.id > id_estudante):
            direita = meio - 1
        else:
            esquerda = meio + 1

    print(f"O estudante de ID '{id_estudante}' não foi encontrado")
    return None

pesquisaBinaria()