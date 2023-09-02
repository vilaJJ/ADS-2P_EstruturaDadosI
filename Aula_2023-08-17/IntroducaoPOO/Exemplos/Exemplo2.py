'''
Crie uma classe chamada Retangulo, que possui duas propriedades: base e altura.

A classe deverá possuir os métodos calcularArea() e calcularPerimetro().
'''

class Exemplo2:
    def __init__(self) -> None:
      pass
    
    def executar(self):
        # Instanciar objetos:
        retangulo1 = Retangulo(15, 10)
        retangulo2 = Retangulo(8, 4)

        # Utilizar os métodos das instâncias
        print(f"Área do retangulo1: {retangulo1.calcularArea()} metros")
        print(f"Área do retangulo2: {retangulo2.calcularArea()} metros\n")

        print(f"Perimetro do retangulo1: {retangulo1.calcularPerimetro()} metros")
        print(f"Perimetro do retangulo2: {retangulo2.calcularPerimetro()} metros\n")
  

class Retangulo:
  # Método inicializador
  def __init__(self, base, altura):
    self.base = base
    self.altura = altura

  def calcularArea(self):
    return (self.base * self.altura)

  def calcularPerimetro(self):
    return ((self.base * 2) + (self.altura * 2))