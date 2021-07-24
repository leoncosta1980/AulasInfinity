from Refeicao import Refeicao
from Voo import Voo, calculaPercPaxBC, calculaPercPaxYC

numeroVoo = int(input("Digite o número do vôo: "))
paxBC = int(input("Informe o número de Passageiros BC: "))
paxYC = int(input("Informe o número de Passageiros YC: "))

calculaPercPaxBC(paxBC)
calculaPercPaxYC(paxYC)

prato1 = Refeicao("fileMignon", "arrozPrimavera","batataGomo")
prato2 = Refeicao("fraldinhaWessel", "arrozBranco", "batataGratin", "molhoDemig")
prato3 = Refeicao("picanhaGrelh","arrozSalsa","aboboraPali","molhoBarbecue" )
prato4 = Refeicao("fileMignon", "risotoPrim","brocolis")

pratos = [prato1, prato2, prato3, prato4]

#Refeicao = Refeicao(pratos)

#Voo.calculaPrato1(prato1)

v1 = Voo(numeroVoo, paxBC, paxYC, pratos)
#print(v1.refeicao.proteina)
#v1.visualizaPrato()
v1.calculaPeso()