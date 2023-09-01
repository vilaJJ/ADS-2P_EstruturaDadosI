'''
e) Imprima todos os divisores de determinado número.
'''

class Questao5:
    def exibir_barras(self):
        print("=" * 50)
        return
    
    def exibir_divisores(self, numero):
        self.exibir_barras()
        print(f"Exibindo divisores de {numero}:")
        for i in range (1, numero + 1):
            if(numero % i == 0):
                print(i)
        self.exibir_barras()
        return
    
    def executar(self):
        numero = int(input("Insira um valor inteiro, para descobrir os seus divisores: "))
        self.exibir_divisores(numero)
        return
        