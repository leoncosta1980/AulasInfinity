class Instrumento:
    def __init__(self, nome, grauDificuldade, professor):
        self._nome = nome
        self._grauDificuldade = grauDificuldade
        self._professor = professor
        
    def dificuldade(self):
        return self._grauDificuldade - self._professor.pontuacao
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,novoNome):
        self._nome = novoNome
    
    @property
    def grauDificuldade(self):
        return self._grauDificuldade
    
    @grauDificuldade.setter
    def grauDificuldade(self,novoGrauDificuldade):
        self._grauDificuldade = novoGrauDificuldade
    
    @property
    def professor(self):
        return self._professor.nome
    
    @nome.setter
    def nome(self,novoProfessor):
        self._nome = novoProfessor
    
    