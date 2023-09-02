'''
/PROBLEMA    1002 - Área do Círculo

# include <stdio.h>
int main() {
    double raio, area;
    scanf("%lf", &raio);
    area = (3.14159 * (raio * raio));
    printf("A=%.4lf\n", area);
    return 0;
}
'''

import math

class Questao2:
    def calcularAreaCirculo(self, raio):
        pi = 3.14159
        return (pi * (math.pow(raio, 2)))
    
    def executar(self):
        raio = float(input("Insira o raio do círculo: "))
        print("A={0:.4f}\n".format(self.calcularAreaCirculo(raio)))
        return