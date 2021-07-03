from Funcionario import Funcionario
from FolhaPagamentoRH import FolhaPagamentoRH

f1 = Funcionario("Matheus", 3000, "0001", "Operador de Testes")
f2 = Funcionario("Matheus", 5000, "0002", "Arquiteto de Software")

funcionarios = [f1, f2]

folhaDePagamentos = FolhaPagamentoRH(funcionarios)

print(folhaDePagamentos.gastos())