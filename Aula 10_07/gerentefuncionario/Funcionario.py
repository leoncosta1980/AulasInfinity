class Funcionario:
    def __init__(self,nome, cpf, salario):
        self._nome = nome
        self._cpf = cpf
        self._salario = salario
        
    def salario_liquido(self, descontos):
        liquido = self._salario
        for item in descontos:
            liquido -= item
        return liquido
    
    def bonificar(self):
        return self._salario * 0.1
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def cpf(self):
        return self._cpf
    
    @property
    def salario(self):
        return self._salario