class ClienteEnd:
    def __init__(self, nome, email, senha, endereço):
        self.nome = nome
        self.email = email
        self.__senha = senha
        self.endereço = endereço
        
    @property
    def senha(self):
        return "*********"
    
    @senha.setter
    def senha(self,novaSenha):
        return