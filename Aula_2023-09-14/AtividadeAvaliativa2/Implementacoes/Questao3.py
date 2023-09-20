from Helpers.ManipularArquivos import ManipularArquivos
from Helpers.Estudante import Estudante
import json

def pesquisaSequencial():
    id_estudante = int(input("Insira o ID do estudante: "))

    manipularArquivos = ManipularArquivos()
    dados_estudantes = manipularArquivos.open("../../LerArquivoSequencial/dados_estudantes.txt")

    for item in dados_estudantes:
        json_estudante = json.loads(item)
        
        if(json_estudante['id'] == id_estudante):
            estudante = Estudante(json_estudante)
            print("\nEstudante encontrado:\n")
            estudante.apresentarInformacoes()
            return estudante
    print(f"O estudante de ID '{id_estudante}' não foi encontrado")
    return None

pesquisaSequencial()