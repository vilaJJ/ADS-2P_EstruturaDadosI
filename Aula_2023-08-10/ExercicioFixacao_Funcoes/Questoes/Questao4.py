'''
d) Indique se um número é divisível por 6.
'''

class Questao4:
    def divisivel_por_seis(self, numero):
        return numero % 6 == 0
    
    def executar(self):
        numero = int(input("Insira um número inteiro, para verificar se ele é divisível por 6: "))
        
        if(self.divisivel_por_seis(numero)):
            print(f"{numero} é divisível por 6.")
        else:
            print(f"{numero} não é divisível por 6.")
        return