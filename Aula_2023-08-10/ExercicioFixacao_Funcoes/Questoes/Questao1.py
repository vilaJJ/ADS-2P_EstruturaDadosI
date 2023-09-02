'''
a) Faça uma saudação a uma pessoa conforme a hora do dia 
-> antes das 12: Bom dia; 
-> entre 12 e 19: Boa tarde;
-> depois das 19: Boa noite.
 
(Dica: utilize a função datetime.now().hour para obter a hora atual)
'''

from datetime import datetime

class Questao1:
    def saudacoes(self):
        hora = datetime.now().hour - 3
        saudacao = "Olá!!\n"

        if(hora < 12):
            saudacao += "Bom dia!!"
        elif(hora < 19):
            saudacao += "Boa tarde!!"
        else:
            saudacao += "Boa noite!!"

        print(saudacao)
        return
    
    def executar(self):
        self.saudacoes()