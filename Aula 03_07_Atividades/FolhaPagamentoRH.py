class folhaPagamento:
    def __init__(self, funcionarios):
        self.__funcionarios = funcionarios
     
     #Metodos
    def gastos (self):
        gastoTotal = 0
        for f in self.__funcionarios:
            gastoTotal += f.salario
        return "Os gastos com funcionários foram de " +str(gastoTotal) + "Reais"  
    
    @property
    def funcionarios(self):
        for f in self.__funcionarios:
            print("Funcionário: ", f.nome, "Salário: ", str(f.salario))
        return True
    
        
    @funcionarios.setter
    def funcionarios(self, novoFuncionario):
        self.__funcionarios.append(novoFuncionario)
        
    