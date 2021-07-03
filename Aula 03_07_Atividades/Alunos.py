class Alunos:
    def __init__(self, nome, semestre, matricula, notas):
        self.nome = nome
        self.semestre = semestre
        self.matricula = matricula
        self.__notas = notas
    
    def score (self):
        contador = 0
        valorTotal = 0
        for n in self.__notas:
            contador += 1
            valorTotal += n.valor
        media = valorTotal / contador
        return media
    
    @property
    def notas(self):
        for n in self.notas:
            print("A nota de ", n.nome + "foi ", str(n.valor))
        return
    
    @notas.setter
    def notas (self, novaNota):
        self.__notas.append(novaNota)