class Jedi:
    def __init__(self, nome, grau, especie, sabre, nomeDaNave = ""):
        self.nome = nome
        self.__grau = grau
        self.especie = especie
        self.sabre = sabre
        self.nomeDaNave = nomeDaNave
    
    
    @property
    def grau(self):
        return self.__grau
    
    @grau.setter
    def grau(self, novoGrau):
        if novoGrau != "Padawan" or novoGrau != "Cavaleiro" or novoGrau != "Mestre":
            return False
        else:
            self.__grau = novoGrau
        