'''
2) Escreva uma função em Python que verifique se existe determinado valor inteiro em um vetor (A função deve retornar a posição da primeira ocorrência do valor ou -1 caso não exista o valor). Além disso, na sua resposta deve existir uma chamada à função criada para testá-la.
'''

class Questao2:
    def vetor_contem_inteiro(self, vetor):
        for i in range(0, len(vetor)):
            if(type(vetor[i]) == int):
                return i
        return -1
    
    def executar(self):
        vetor1 = ["Juan", "Felipe", "Alves", "Flores"]
        vetor2 = ["Python", "Estrutura de Dados", 2023, True]
        vetor3 = [14, 22, 25]
        
        print(self.vetor_contem_inteiro(vetor1))
        print(self.vetor_contem_inteiro(vetor2))
        print(self.vetor_contem_inteiro(vetor3))