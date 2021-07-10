from Funcionario import Funcionario

class Gerente(Funcionario):
    def __init__(self,nome, cpf, salario, senha, qt_gerenciados):
        super().__init__(nome, cpf, salario)
        self.senha = senha
        self.qt_gerenciados = qt_gerenciados
    
    
    def bonifica (self):
        return self._salario * 0.15