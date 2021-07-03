def verificaPlano (plano):
    if plano == "economico" or plano == "estudantil" or plano == "platinum":
        return plano
    else:
        print("Plano inválido")
        return ""

class Clientes:
    def __init__(self, matricula, nome, data_nascimento, plano):
        self.matricula = matricula
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__plano = plano
    
    @property
    def plano(self):
        return "O plano do cliente é: " + self.__plano
    
    @plano.setter
    def plano(self,verificaPlano ):
        self.__plano = verificaPlano