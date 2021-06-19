class ContaCorrente:
    def __init__(self, numero, senha, agencia="520", banco="011", saldo=1500.0):
        self.numero = numero
        self.senha = senha
        self.agencia = agencia
        self.banco = banco
        self.saldo = saldo
        
        
    #Método de saque
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            return True
        else:
            return False
        
    def transferir(self, contaDestino, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            contaDestino.saldo += valor
            return True
        else:
            return False
    
    def depositar(self, valor):
        self.saldo += valor