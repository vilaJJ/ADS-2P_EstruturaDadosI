from Helpers.DataHorario import DataHorario

class Estudante:
    def __init__(self, json_estudante):
        self.id = json_estudante['id']
        self.nome = json_estudante['nome']
        self.emailInstitucional = json_estudante['emailInstitucional']

    def apresentarInformacoes(self):
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Email institucional: {self.emailInstitucional}")
        return
    
    def gerarRelatorioConsulta(self):
        datahorario = DataHorario()

        barraInicial = f"{'-' * 100}\n"
        infoOperacao = f"Consulta realizada em: {datahorario.dataFormatada()}\n\n"
        id = f"ID: {self.id}\n"
        nome = f"Nome: {self.nome}\n"
        emailInst = f"Email institucional: {self.emailInstitucional}\n"
        
        return barraInicial + infoOperacao + id + nome + emailInst
