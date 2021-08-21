import mysql.connector
from mysql.connector import Error

try:
    connector = mysql.connector.connect(
        host='localhost',
        database='aula14082021',
        user='root',
        password='aluno99'
    )
    
    db_info = connector.get_server_info()
    print("Conectou ao mysql versão: ", db_info)
    
    blocoDeNotas=connector.cursor()
    query = "SELECT MATRICULA, NOME, SEXO FROM aluno"
    blocoDeNotas.execute(query)
    
    for (registration, name, gender) in blocoDeNotas:
        print(f"Matricula: {registration}, Nome: {name}, Sexo: {gender}")
        #f-string Formatting in Python
        #http://www.datacamp.com/community/tutorials/f-string-formatting-in-python
        
except Error as e:
    print("Erro ao acessar o mysql: ",e)

