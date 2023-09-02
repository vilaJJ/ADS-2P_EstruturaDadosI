'''
3) Escreva uma função em Python que realize a troca de valores entre duas posições de um vetor (A função deve retornar o vetor atualizado). Além disso, na sua resposta deve existir uma chamada à função criada para testá-la.
'''

import random

class Questao3:
    def trocar_valores_vetor(self, vetor):
        tamanhoVetor = len(vetor)
        if(tamanhoVetor == 0):
            print("Vetor vazio")
            return vetor

        posicao1 = random.randint(0, tamanhoVetor - 1)
        posicao2 = 0
        while(True):
            value = random.randint(0, tamanhoVetor - 1)
            if(value != posicao1):
                posicao2 = value
            break

        print(f"Vetor anterior: {vetor}")
        print(f"Posições trocadas: {posicao1} ({vetor[posicao1]}) e {posicao2} ({vetor[posicao2]})")

        aux = vetor[posicao1]
        vetor[posicao1] = vetor[posicao2]
        vetor[posicao2] = aux

        return vetor
    
    def executar(self):
        print(self.trocar_valores_vetor([3, 17, 23]))
        print("=" * 50)
        print(self.trocar_valores_vetor(["Juan", "Felipe", "Alves", "Flores"]))
        print("=" * 50)
        print(self.trocar_valores_vetor([]))
        print("=" * 50)