from datetime import datetime

class DataHorario:
    def __init__(self) -> None:
        pass
    
    def format(self, value):
        if(value < 10):
            return f"0{value}"
        else:
            return value

    def dataFormatada(self):
        datahorario = datetime.now()

        data = f"{self.format(datahorario.day)}/{self.format(datahorario.month)}/{self.format(datahorario.year)}"
        horario = f"{self.format(datahorario.hour)}:{self.format(datahorario.minute)}:{self.format(datahorario.second)}"
        return f"{data} {horario}"