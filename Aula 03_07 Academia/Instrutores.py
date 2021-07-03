def verificaTurno (turno):
    if turno == "matutino" or turno == "vespertino" or turno == "noturno":
        return turno
    else:
        print("Turno inválido")
        return ""

def verificaCategoria (categoria):
    if categoria == "musculacao" or categoria == "crossfit" or categoria == "spinning":
        return categoria
    else:
        print("Categoria inválida")
        return ""


class Instrutores:
    def __init__(self, codigo, nome, data_nascimento, salario, turno, cref, categoria):
        self.codigo = codigo
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.__salario = salario
        self.__turno = turno
        self.cref = cref
        self.__categoria = categoria
    
    @property
    def salario(self):
        return "O salário do Instrutor é: " + str(self.__salario)
    
    @salario.setter
    def salario(self,novoSalario):
        print("Não é possível atribuir novo salário")
        
    @property
    def turno(self):
        return "O turno do Instrutor é: " + self.__turno
    
    @turno.setter
    def turno(self,novoTurno):
        self.turno(verificaTurno)
        
    @property
    def categoria(self):
        return "A categoria do Instrutor é: " + self.__categoria
    
    @turno.setter
    def categoria(self,novaCategoria):
        self.categoria(verificaCategoria)