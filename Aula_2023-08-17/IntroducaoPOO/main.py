'''
Exemplos desenvolvidos na aula.
'''

from Exemplos.Exemplo1 import Exemplo1
from Exemplos.Exemplo2 import Exemplo2

def main():
    while True:
        questao = int(input("Insira o exemplo 1 ou 2 para executar (0 encerra): "))
        
        if(questao == 0):
            print("\nPrograma encerrado!")
            return
        elif(questao == 1):
            exemplo1 = Exemplo1()
            exemplo1.executar()
            return
        elif(questao == 2):
            exemplo2 = Exemplo2()
            exemplo2.executar()
            return
        else:
            print("\nValor inválido. Tente novamente!\n")
            
main()