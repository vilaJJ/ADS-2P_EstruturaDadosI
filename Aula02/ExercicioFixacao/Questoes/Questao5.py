'''
# include <stdio.h>

int main(){
  float n1, n2,media;
  do {
    scanf("%f", &n1);
    if (!(n1 >= 0.0 && n1 <=10.0)) {
      printf("nota invalida\n");
    }
  } while (!(n1 >= 0.0 && n1 <=10.0));

  do {
    scanf("%f", &n2);
    if (!(n2 >= 0.0 && n2 <=10.0)) {
      printf("nota invalida\n");
    }
  } while (!(n2 >= 0.0 && n2 <=10.0));

  media = (n1+n2) / 2.0;
  printf("media = %.2f\n", media);
  return 0;
}
'''

class Questao5:
    def nota_valida(self, nota):
        retorno = (nota >= 0 and nota <= 10)
        if(retorno is False): print("Nota inválida! Tente novamente.\n")
        return retorno
    
    def inserir_valor(self, texto):
        while True:
            valor = float(input(texto))
            if(self.nota_valida(valor)):
                return valor
    
    def calcular_nota(self, nota1, nota2):
        return ((nota1 + nota2) / 2)
    
    def executar(self):
        nota1 = self.inserir_valor("Insira a nota 1: ")
        nota2 = self.inserir_valor("Insira a nota 2: ")
        
        media = self.calcular_nota(nota1, nota2)
        print("Média: {0:.2f}".format(media))
        return