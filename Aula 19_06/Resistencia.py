class Resistencia:
    def __init__(self, nome, especie, cargo, nomeDaNave = ""):
        self.nome = nome
        self.especie = especie
        self.__cargo = cargo
        self.nomeDaNave = nomeDaNave
        
    
    @property
    def cargo(self):
        return self.__cargo
    
    @cargo.setter
    def cargo(self, novoCargo):
        if novoCargo != "Mecânico" or novoCargo != "Piloto" or novoCargo != "Instrutor":
            return False
        else:
            self.__cargo = novoCargo