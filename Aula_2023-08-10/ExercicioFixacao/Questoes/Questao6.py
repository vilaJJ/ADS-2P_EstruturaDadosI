'''
# include <stdio.h>
int main ()
{
    for (int i = 0; i < 10; i++)
    {
        printf (“%d", i);
    }
    return 0;
}
'''

class Questao6:
    def executar(self):
        for num in range(10):
            print("{0}".format(num))
        return