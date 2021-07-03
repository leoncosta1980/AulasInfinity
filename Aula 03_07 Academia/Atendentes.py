def verificaTurno (turno):
    if turno == "matutino" or turno == "vespertino" or turno == "noturno":
        return turno
    else:
        print("Turno inválido")
        return ""
    
class Atendentes:
    #construtor
    def __init__(self, codigo, nome, data_nascimento, salario, turno):
        self.codigo = codigo
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__salario = salario
        self.__turno = verificaTurno(turno)
    
    @property
    def salario(self):
        return "O salário do atendente é: " + str(self.__salario)
    
    @salario.setter
    def salario(self,novoSalario):
        print("Não é possível atribuir novo salário")
        
    @property
    def turno(self):
        return "O turno do atendente é: " + self.__turno
    
    @turno.setter
    def turno(self,novoTurno):
        self.__turno = verificaTurno(novoTurno)