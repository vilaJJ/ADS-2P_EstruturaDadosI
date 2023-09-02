'''
g) Imprima os valores ímpares de um vetor.
'''

class Questao7:
    def valores_impares_vetor(self, vetor):
        retorno = []
        for i in vetor:
            if(i % 2 == 1):
                retorno.append(i)
        return retorno
    
    def digitar_vetor(self):
        retorno = []
        length = int(input("Insira um valor inteiro, para definir o tamanho do vetor: "))
        for i in range(length):
            retorno.append(int(input(f"Insira o {i + 1}° valor: ")))
        return retorno
    
    def executar(self):
        print("\nValores ímpares em um vetor\n")
        vetor = self.digitar_vetor()
        vetor_valores_impares = self.valores_impares_vetor(vetor)
        
        print(f"Vetor original: {vetor}")
        print(f"Vetor apenas com valores ímpares: {vetor_valores_impares}")
        return