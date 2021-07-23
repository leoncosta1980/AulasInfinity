from Refeicao import Refeicao

class Jantar(Refeicao):
    def __init__(self, proteinas, legumes, graos, molho, paes, sobremesa, sopa):
        super().__init__(proteinas, legumes, graos, molho)
        self.__paes = paes
        self.__sobremesa = sobremesa
        self.__sopa = sopa
        
        
    @property
    def paes(self):
        return self.__paes
    @paes.setter
    def paes(self, paes):
        self.__paes = paes
        
    @property
    def sobremesa(self):
        return self.__sobremesa
    @sobremesa.setter
    def sobremesa(self, sobremesa):
        self.__sobremesa = sobremesa
              
    @property
    def sopa(self):
        return self.__sopa
    @sopa.setter
    def sopa(self, sopa):
        self.__sobremesa = sopa