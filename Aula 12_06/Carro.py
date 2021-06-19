class Carro:
    def __init__(self,marca, modelo, ano, velocidade, ligado=False, automatico=False):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.velocidade = velocidade
        self.ligado = ligado
        self.automatico = automatico
    
    def ligar (self):
        self.ligado = True
    
    def desligar (self):
        if self.desligado==True:
            self.desligado = False
    
    def acelerar (self, valor):
        if self.ligado==True:
            if valor <= 120:
                self.velocidade += valor
                return True
            else:
                self.ligado = False
                return False
                
    def verificarMarcha (self):
        if (self.velocidade > 120):
            return self.desligar()
        elif self.velocidade <= 19:
            return 1
        elif (self.velocidade >=20 and self.velocidade <= 29):
            return 2
        elif (self.velocidade >=30 and self.velocidade <= 44):
            return 3
        elif (self.velocidade >=44 and self.velocidade <= 59):
            return 4
        elif (self.velocidade >=60 and self.velocidade <=120):
            return 5
        
        