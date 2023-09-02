class Exemplo1:
    def __init__(self) -> None:
        pass
    
    def executar(self):
        # Instanciar objetos
        produto1 = Produto("Xiaomi Poco X3 Pro")

        # Utilizar os métodos da instância
        produto1.comprar(15)
        produto1.vender(7)
        produto1.renomear("Xiaomi Poco X3 Pro (Vayu)")

        # Exibir as propriedades
        print(produto1.nome)
        print(produto1.estoque)

# Classe desenvolvida para explicação de POO em Python
class Produto:
  # Método inicializador
  def __init__(self, nome):
    # Definir o nome de uma propriedade, precedemos da palavra self
    self.nome = nome
    self.estoque = 0

  def comprar(self, quantidade):
    self.estoque += quantidade

  def vender(self, quantidade):
    self.estoque -= quantidade

  def renomear(self, nome):
    self.nome = nome