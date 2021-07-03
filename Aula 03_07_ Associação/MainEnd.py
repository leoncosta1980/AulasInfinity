from ClienteEnd import ClienteEnd
from Endereço import Endereço

e1 = Endereço("41111-600" "Rua K", "Itapuã", "300", "Salvador", "Bahia", "Brasil", "casa 1")
c1 = ClienteEnd("Marlene", "mam_souza@gmail.com", "12345", e1)

print(c1.endereço.cep)