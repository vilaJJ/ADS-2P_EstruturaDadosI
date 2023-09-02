'''
# include <stdio.h>

int main(){
  int km, minutos;
  scanf("%d", &km);
  minutos = km * 2;
  printf("%d minutos\n", minutos);
  return 0;
}
'''

class Questao4:
    def executar(self):
        km = int(input("Insira as horas (inteiro): "))
        minutos = km * 2
        print("{0} minutos\n".format(minutos))
        return