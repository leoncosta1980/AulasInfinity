from Candidato import Candidato
from Prova import Prova
from Processo import Processo

p1 = Prova("02/06/2021", 9)

c1 = Candidato("Matheus", "Rua K,", 5, "Estudante de Ciencias", p1)
candidatos = [c1]

processo = Processo(candidatos)
processo.aprovados()
