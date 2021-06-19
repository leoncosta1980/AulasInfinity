from Carro import Carro

carro1 = Carro("Fiat","Strada","2020",0)

carro1.ligar()

# carro1.acelerar(int(input("Informe quanto deseja acelerar: ")))

# if carro1.verificarMarcha() == False:
#     print("Baixar velocidade")
# else:
#     print("O carro está na ",carro1.verificarMarcha(), "ª marcha")

if carro1.acelerar(int(input("Informe quanto deseja acelerar: "))):
    print("Acelerou")
else:
    print("Não acelerou")
    