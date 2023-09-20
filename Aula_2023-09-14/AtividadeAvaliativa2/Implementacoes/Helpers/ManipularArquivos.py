from os import path

class ManipularArquivos:
    def __init__(self):
        self.caminho_programa = path.dirname(__file__)

    def open(self, caminho_relativo):
        caminho_completo = path.join(self.caminho_programa, caminho_relativo)

        return open(caminho_completo)
    
    def gravar(self, caminho_relativo, conteudo):
        caminho_completo = path.join(self.caminho_programa, caminho_relativo)     
        
        infosExistentes = ""
        if(path.exists(caminho_completo)):
            arquivoLeitura = open(caminho_completo, "r")
            infosExistentes = arquivoLeitura.read()

        arquivoGravacao = open(caminho_completo, "w")
        arquivoGravacao.write(infosExistentes + conteudo)
        arquivoGravacao.close()

        print("\nRegistro de pesquisa salvo com sucesso")
        return True