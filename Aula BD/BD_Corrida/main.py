from banco import Banco
from Atleta import Atleta
from AtletaBD import AtletaBD


conexao = Banco()
con = conexao.conectar()
a = AtletaBD(con)

i="s"
while i == "s":
    nome = input("Nome: ")
    idade = input("Idade: ")
    atleta = Atleta(nome, idade)
   
    resultado = a.insereAtletas(atleta)
    print(resultado)
    i=(input("Deseja Inserir mais uma Atleta? [s/n] "))
   
atletas = a.listaAtletas()
if atletas!= None:
    for (id,nome,idade) in atletas:
        print(f"ID: {id}")
        print(f"Nome: {nome}")
        print(f"Idade: {idade}")
        print("==================")
