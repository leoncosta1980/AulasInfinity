class Funcionario:
    def __init__(self, nome, salario, matricula, funcao):
        self.nome = nome
        self.__salario = salario
        self.matricula = matricula
        self.funcao = funcao
    
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario (self, valor):
        #aumento = self.__salario * 0.20
        novoSalario = self.__salario * 1.20
    
        if novoSalario >= valor and valor > self.__salario:
            self.__salario = valor
        