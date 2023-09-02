'''
b) Calcule o resto da divisão entre dois números (sem utilizar o operador padrão). 
(Dica: faça o processo no papel e observe cada passo)
'''

class Questao2:
    def resto_divisao(self, divisor, dividendo):
        while divisor >= dividendo:
            divisor -= dividendo
        return divisor
    
    def executar(self):
        print("\nExecutando resto da divisão:\n")
        
        divisor = float(input("Insira o divisor: "))
        dividendo = float(input("Insira o dividendo: "))
        
        print(f"Resto da divisão: {self.resto_divisao(divisor, dividendo)}")
        return