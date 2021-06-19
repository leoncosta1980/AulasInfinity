print("Olá Mundo!")
print("Bem vindo!")
print("------------------------------------------------------------------")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura*altura)

print("Seu IMC é: {:.2f}".format(imc))

print("------------------------------------------------------------------")

temperaturaFarenheit = float(input("Digite a temperatura em Farenheit: "))
temperaturaCelsius = (temperaturaFarenheit - 32)*5/9
print ("A temperatura em °C é: {}".format(temperaturaCelsius))

print("------------------------------------------------------------------")

base = float(input("Digite o valor da base: "))
altura = float(input("Digite o valor da altura: "))
print("A área é {}".format(base*altura))

print("------------------------------------------------------------------")

totalValidos = int(input("Digite o total de votos válidos: "))
votosBrancos = int(input("Digite o total de votos brancos: "))
votosNulos = int(input("Digite o total de votos nulos: "))
totalEleitores = totalValidos + votosBrancos + votosNulos
print("O Total de Eleitores é {:.2f}".format(totalEleitores))
print("O Percentual de votos Válidos é: {:.2f}%".format((totalValidos/totalEleitores)*100))
print("O Percentual de votos Brancos é: {:.2f}%".format((votosBrancos/totalEleitores)*100))
print("O Percentual de votos Nulos é: {:.2f}%".format((votosNulos/totalEleitores)*100))

print("------------------------------------------------------------------")

a = input("Digite o valor de a: ")
b = input("Digite o valor de b: ")

c = a
a = b
b = c
print("O valor de a é: ",a, "e o valor de B é:",b)

print("------------------------------------------------------------------")

custoFabrica = float(input("Digite o custo de Fábrica do veículo: "))
custocomImposto = custoFabrica + (custoFabrica*0.45)
custoDistribuidor = custoFabrica + (custoFabrica*0.28)
custoTotal = custoFabrica + custocomImposto + custoDistribuidor
print("O custo total ao consumidor é R$ {:.2f}".format(custoTotal))

print("------------------------------------------------------------------")

print("Olá Mundo")

