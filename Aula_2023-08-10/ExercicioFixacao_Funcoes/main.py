'''
Atividade de fixação funções em Python:
    Construir funções
'''

from Questoes.Questao1 import Questao1
from Questoes.Questao2 import Questao2
from Questoes.Questao3 import Questao3
from Questoes.Questao4 import Questao4
from Questoes.Questao5 import Questao5
from Questoes.Questao6 import Questao6
from Questoes.Questao7 import Questao7

def main():
    while True:
        questao = int(input("Insira uma questão de 1 à 7 para executar (0 encerra): "))
        
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
            return
        elif(questao == 4):
            questao4 = Questao4()
            questao4.executar()
            return
        elif(questao == 5):
            questao5 = Questao5()
            questao5.executar()
            return
        elif(questao == 6):
            questao6 = Questao6()
            questao6.executar()
            return
        elif(questao == 7):
            questao7 = Questao7()
            questao7.executar()
            return
        else:
            print("\nValor inválido. Tente novamente!\n")
            
main()