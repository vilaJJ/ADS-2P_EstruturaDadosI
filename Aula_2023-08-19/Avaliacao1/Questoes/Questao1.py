'''
1) Escreva uma função em Python, a seu critério, que atenda os seguintes requisitos:

i. o código deve conter no mínimo 5 linhas de instrução (sem contar comentários);
ii. o código deve conter pelo menos um estrutura de decisão ou repetição;
iii. realize comentários no seu código explicando a função do algoritmo e de cada instrução escrita.
'''

# Média aritmética

class Questao1:
    def media_aritmetica(self):
        # Exibe uma mensagem indicando como sair do loop de inserção
        print("Bem-vindo a calculadora de média aritmética!\nDigite '-1' quando desejar encerrar a inserção.\n")

        # Variáveis utilizadas: 'valores' será onde os dados de entrada serão armazenados; 'media' é o retorno
        valores = []
        media = 0

        # While com valor lógico sempre verdadeiro, só será quebrado quando ocorrer o break
        while(True):
            # Pede ao usuário que insira um valor númerico
            value = float(input("Insira um valor númerico: "))
            # Analisa se o usuário inseriu o valor de saída do loop
            if(value == -1):
                # Quebra o loop
                break
            else:
                # Adiciona ao vetor o valor digitado pelo usuário anteriormente
                valores.append(value)

        # Exibe o vetor por completo
        print(f"\nVetor inserido: {valores}")

        # Estrutura de repetição responsável por somar os valores inseridos
        for i in range(0, len(valores)):
            # Os valores estão sendo somados e inseridos na variável 'media'
            media += valores[i]

        # Divide os valores somados pela quantidade de valores inseridos
        media = media / len(valores)

        # Realiza o retorno da função, devolvendo o valor da média aritmética.
        return media
    
    def executar(self):
        media = self.media_aritmetica()
        print(f"Média = {media}")