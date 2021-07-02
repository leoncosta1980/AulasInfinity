class Atendentes:
    def __init__(self, codigo, nome, data_nascimento, salario, turno):
        self.nome = nome
        self.codigo = codigo
        self.data_nascimento = data_nascimento
        self.__salario = salario
        self.turno = turno
