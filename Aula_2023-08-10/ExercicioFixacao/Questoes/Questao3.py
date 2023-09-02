'''
//PROBLEMA    1035 - Teste de Seleção 1

# include <stdio.h>
int main() {
    int A, B, C, D;
    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &C);
    scanf("%d", &D);
    if(B > C && D > A && (C + D) > (A+B) && C>=0 && D>=0 && A%2==0){
        printf("Valores aceitos\n");
    }
    else{
        printf("Valores não aceitos\n");
    }
    return 0;
}
'''

class Questao3:
    def inserir_valor(self, letra): return int(input("Insira o valor de {0}: ".format(letra)))

    def executar(self):
        A = self.inserir_valor("A")
        B = self.inserir_valor("B")
        C = self.inserir_valor("C")
        D = self.inserir_valor("D")

        condicao = ((B > C) and (D > A) and ((C + D) > (A + B)) and (C >= 0) and (D >= 0) and ((A % 2) == 0))

        if (condicao):
            print("Valores aceitos\n")
        else:
            print("Valores não aceitos\n")
            
        return