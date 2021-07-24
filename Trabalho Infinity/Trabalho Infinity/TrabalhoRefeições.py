print('{:=^40}'.format(' SERVIÇO DE BORDO '))

nVoo = int(input("Informe número do vôo: "))
while nVoo == 0:
    print ("Vôo Inexistente!")
    nVoo = int(input("\nInforme número do vôo: "))

qtPaxBC = int(input("Informe a quantidade de passageiros BC: "))

   
opPrato1 = qtPaxBC * 0.6
opPrato2 = qtPaxBC * 0.4

print ("Quantidade de pratos op1: {:.2f}".format (round(opPrato1)))
print ("Quantidade de pratos 0p2: {:.2f}".format (round(opPrato2)))

qtPaxYC = int(input("Informe a quantidade de passageiros YC: "))

opPrato3 = qtPaxYC * 0.7
opPrato4 = qtPaxYC * 0.3

print ("Quantidade de pratos op3: {:.2f}".format (round(opPrato3)))
print ("Quantidade de pratos 0p4: {:.2f}".format (round(opPrato4)))

print('{:=^40}'.format(' COMPOSIÇÃO DO PRATO '))

# prato1 = 1
fileMignon = 0.140
arrozPrimavera = 0.1
batataGomo = 0.05
tomateSweet = 4

#prato2 = 2
fraldinhaWessel = 0.140
molhoDemig=0.03
arrozBranco=0.1
batataGratin=0.06
cenouraPalito=4

#prato3 = 3
picanhaGrelh = 0.140
farofaOvos=0.03
arrozSalsa=0.1
aboboraPali=0.06
molhoBarbecue=0.03

#prato4 = 4
risotoPrim = 0.3
brocolis = 0.06
fileMignon = 0.140

# laco inicializado como True, roda enquanto for True ou ate ser interrompido
while True:
    opc = int(input("\nInsira a opcao de prato a ser consultada ou 0 para sair: "))
    if opc == 1:
        print("\nA Opção 1 será:\n \n***Filé Mignon com Arroz Primavera, Batata Gomo Assada e Tomate Sweet Grape.")
        print("\nPara preparar esta receita serão necessários: \n\nFilé Mignon: {:.2f} Kg \nArroz: {:.2f} kg \nBatata: {:.2f} Kg \nTomate Sweet Grape: {:.2f} unidades".format(fileMignon*opPrato1, arrozPrimavera*opPrato1, batataGomo*opPrato1, tomateSweet*opPrato1))
    elif opc == 2:
        print("\nA Opção 2 será:\n \n***Fraldinha Braseada Fatiada ao Molho Demiglace, Arroz Branco, Batata Gratinada e Cenoura Palito.")
        print("\nPara preparar a receita 2 serão necessários: \n\nFraldinha Wessel: {:.2f} Kg \nMolho Demiglace: {:.2f} Kg \nArroz Branco: {:.2f} Kg \nBatata Gratinada: {:.2f} kg \nCenoura Palito: {:.2f} Un".format(fraldinhaWessel*opPrato2, molhoDemig*opPrato2, arrozBranco*opPrato2, batataGratin*opPrato2, cenouraPalito*opPrato2 ))
    elif opc == 3:
        print("\nA Opção 3 será:\n \n***Picanha Grelhada ao Molho Barbecue com Farofa de Ovos, Arroz com Salsa e Abóbora Palito Blancheada.")
        print("\nPara preparar a receita 3 serão necessários: \n\nPicanha: {:.2f} Kg \nMolho Barbecue: {:.2f} Kg \nFarofa de Ovos: {:.2f} Kg \nArroz com Salsa: {:.2f} kg \nAbóbora Palito: {:.2f} Kg".format(picanhaGrelh*opPrato3, molhoBarbecue*opPrato3, farofaOvos*opPrato3, arrozSalsa*opPrato3, aboboraPali*opPrato3 ))
    elif opc == 4:
        print("\nA Opção 4 será:\n \n***Risoto primavera com brócolis ao vapor e filé mignon marinado ao molho de ervilhas.")
        print("\nPara preparar a receita 4 serão necessários: \n\nRisoto primavera: {:.2f} Kg \nBrócolis ao vapor: {:.2f} Kg \nFilé Mignon marinado ao molho de ervilhas {:.2f} Kg".format(risotoPrim*opPrato4, brocolis*opPrato4, fileMignon*opPrato4))
    elif opc == 0:
        # se opcao for 0 a funcao break quebra o laco e finaliza o programa
        break
    else:
        print("Opcao invalida, tente novamente!")