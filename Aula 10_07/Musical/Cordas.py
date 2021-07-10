from Instrumento import Instrumento

class Cordas(Instrumento):
    def __init__(self, nome, grauDificuldade, professor, qtdeCordas, tipoCorda):
        super().__init__(nome, grauDificuldade, professor)
        self.qtdeCordas = qtdeCordas
        self.tipoCorda = tipoCorda
        
    def dificuldade(self):
        if self.tipoCorda == "Aço":
            return (self.grauDificuldade * self.qtdeCordas) - self._professor.pontuacao
        else:
            return self._grauDificuldade - self._professor.pontuacao
    