from Instrumento import Instrumento

class Percussao(Instrumento):
    def __init__(self, nome, grauDificuldade, professor, usaBaqueta):
        super().__init__(nome, grauDificuldade, professor)
        self.usaBaqueta = usaBaqueta
        