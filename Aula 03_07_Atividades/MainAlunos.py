from Alunos import Alunos
from Notas import Notas

n1 = Notas("Nota1", "Álgebra Linear", 8.0)
n2 = Notas("Nota2", "Álgebra Linear", 3.0)

notas = [n1, n2]

a1 = Alunos("Matheus", 6, "0001", notas)
n3 = Notas("Nota3","Álgebra Linear", 7.0)

a1.Notas = n3
print(a1.notas)