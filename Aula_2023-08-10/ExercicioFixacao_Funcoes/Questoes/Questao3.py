'''
c) Verifique se um número é primo.
'''

class Questao3:
    def numero_primo(self, numero):
        for i in range(2, numero):
            if(numero % i == 0):
                return False
        return True
    
    def executar(self):
        numero = int(input("Insira um número inteiro, para verificar se é primo: "))
        
        if(self.numero_primo(numero)):
            print(f"{numero} é número primo!")
        else:
            print(f"{numero} não é número primo!")
        return            