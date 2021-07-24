def verificaVoo(numeroVoo):
    if numeroVoo == 0:
        print("Vôo inexistente!")
        pass            
    else:
        print("Número do Vôo é: ",numeroVoo)
        return numeroVoo
            
                    
def calculaPercPaxBC(paxBC):
    Perc1 = paxBC * 0.60
    Perc2 = paxBC * 0.40
    print ("Quantidade de pratos op1: {:.2f}".format (round(Perc1)))
    print ("Quantidade de pratos 0p2: {:.2f}".format (round(Perc2)))
    return ""

def calculaPercPaxYC(paxYC):
    Perc3 = paxYC * 0.70
    Perc4 = paxYC * 0.30
    print ("Quantidade de pratos op1: {:.2f}".format (round(Perc3)))
    print ("Quantidade de pratos 0p2: {:.2f}".format (round(Perc4)))
    return ""
    

class Voo:
    def __init__(self, numeroVoo, paxBC, paxYC, refeicao):
        self.numeroVoo = verificaVoo(numeroVoo)
        self.paxBC = paxBC
        self.paxYC = paxYC
        self.refeicao = refeicao
    
    def visualizaPrato(self):
        for r in self.refeicao:
            print (r.proteina) 
            print (r.acomp1)
            print (r.acomp2)
            print (r.molho)
            print ("--------------------")
               
    def calculaPeso(self):
        for r in range(2):
            print("Será necessário", (self.paxBC * 0.60) * 0.140," Kg de", self.refeicao[r].proteina)