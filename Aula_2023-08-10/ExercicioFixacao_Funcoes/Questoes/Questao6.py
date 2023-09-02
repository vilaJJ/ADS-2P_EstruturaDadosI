'''
f) Verifique se um número é par.
'''

class Questao6:
    def numero_par(self, numero):
        return numero % 2 == 0
    
    def executar(self):
        numero = int(input("Insira um valor inteiro, para descobrir se ele é par ou impar: "))
        resultado = "par" if self.numero_par(numero) else "impar"
        print(f"\n{numero} é {resultado}.")
        return