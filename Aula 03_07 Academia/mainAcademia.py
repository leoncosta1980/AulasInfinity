from Atendentes import Atendentes
from Instrutores import Instrutores
from Clientes import Clientes

a1 = Atendentes("01", "Marcelo", "12/12/1980", 1200, "madrugada")
print (a1.turno)
a1.turno = "noturno"
print (a1.turno)

i1 = Instrutores("02", "Joel", "08/03/1980", 2000, "vespertino", "12345", "crossfit")

c1 = Clientes("0001", "José", "10/07/2003", "estudantil")