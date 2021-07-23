#from abc import ABC, abstractmethod

class Refeicao():
    def __init__(self, proteinas, legumes, graos, molho):
        self._proteinas = proteinas 
        self._legumes = legumes
        self._graos = graos
        self._molho = molho
        
    #@abstractmethod
    #def cadastroPrato(self):
    #    pass
    
    @property
    def proteina(self):
        return self._proteina
    
    @proteina.setter
    def proteina(self, novaProteina):
        self._proteina = novaProteina
        
    @property
    def legumes(self):
        return self._legumes
    
    @legumes.setter
    def legumes(self, novaLegumes):
        self._legumes = novaLegumes
        
    @property
    def graos(self):
        return self._graos
    
    @graos.setter
    def graos(self, novoGraos):
        self._graos = novoGraos
        
    @property
    def molho(self):
        return self._molho
    
    @molho.setter
    def molho(self, novoMolho):
        self._molho = novoMolho
        
        
        
    
    
        
    
    
        
    
        
        
    