class ProdutoAssoc:
    def __init__(self, nome, preco, descricao):
        self.nome = nome
        self.__preco = preco
        self.descricao = descricao
    
    @property
    def preco(self):
        return "R$" + str(self.__preco)
    
    @preco.setter
    def preco(self,novoPreco):
        precoMin = self.__preco - (self.__preco * 0.10)
        
        if precoMin <= novoPreco:
            self.__preco = novoPreco
            return True
        else:
            return False