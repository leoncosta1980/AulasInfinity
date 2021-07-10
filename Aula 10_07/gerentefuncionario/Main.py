from Gerente import Gerente

g1 = Gerente("Marcos", "999.999.999-99", 6000, "12345", 20)

ir = 200
inss = 200
ps = 600

descontos = [ir, inss, ps]
print("O salário será de: R$ " + str(g1.salario_liquido(descontos)))

print("O bonus será de: R$ " +str(g1.bonifica()))
print(g1.nome)
