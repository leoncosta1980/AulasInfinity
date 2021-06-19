from ContaCorrente import ContaCorrente

conta = ContaCorrente("19999", "admin")
conta2 = ContaCorrente("20000","admin")

print("Saldo da Conta:", conta.saldo)
print("Saldo da Conta:", conta2.saldo)

op=int(input("\nInforme a opração que deseja realizar: 1 - Sacar / 2 - Transferir / 3 - Depositar"))


if op == 1:
    if conta.sacar(float(input("Informe o valor do saque: "))):
        print("Saque realizado com sucesso")
    else:
        print("Saldo insuficiente")
elif op == 2:
    if conta.transferir(conta2, float(input("Informe o valor: "))):
        print("Transferência realizada com sucesso")
    else:
        print("Saldo insuficiente")
elif op==3:
    if conta.depositar(float(input("Informe o valor: "))):
        print("Depósito realizado com sucesso")
    else:
        print("Saldo insuficiente")
