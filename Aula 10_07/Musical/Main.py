from Professor import Professor
from Cordas import Cordas
from Percussao import Percussao
from Sopro import Sopro

p1 = Professor("Mozart", 7)

i1 = Cordas("Violão", 5, p1, 6, "Aço")
i2 = Percussao("Bateria", 7, p1, True)
i3 = Sopro("Flauta", 5, p1)

print("O nome do professor é " +p1.nome + " e a sua pontuação é " +str(p1.pontuacao))

print("O grau de dificuldade do instrumento " +i1.nome + "é " +str(i1.dificuldade()))