'''
Atividade Avaliativa 1 - 1º Bimestre

Responda as questões abaixo. (Observação: todos os algoritmos devem ser testados, ou seja, as funções devem ser chamadas)
'''

from Questoes.Questao1 import Questao1
from Questoes.Questao2 import Questao2
from Questoes.Questao3 import Questao3

def main():
    while True:
        questao = int(input("Insira as questões de 1 à 8 para executar (0 encerra): "))
        
        if(questao == 0):
            print("\nPrograma encerrado!")
            return
        elif(questao == 1):
            questao1 = Questao1()
            questao1.executar()
            return
        elif(questao == 2):
            questao2 = Questao2()
            questao2.executar()
            return
        elif(questao == 3):
            questao3 = Questao3()
            questao3.executar()
        else:
            print("\nValor inválido. Tente novamente!\n")
            
main()