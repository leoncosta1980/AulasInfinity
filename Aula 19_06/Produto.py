class Produto:
    def __init__(self, nome, preco, decricao = ""):
        self.nome = nome
        self.__preco = preco
        self.decricao = decricao

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        preco_min = self.__preco * 0.1
        preco_min = self.__preco - preco_min
        if preco_min <= preco:
            self.__preco = preco
        