import mysql.connector
from mysql.connector import Error

class Banco:
    def __init__(self):
        pass
    
    def conectar(self):
        try:
            con = mysql.connector.connect(host='localhost', database='db_corrida',user='root', password='aluno99')
            if con.is_connected():
                print("Conectou!")
                return con
        except Error as e:
            print("Erro na conexão mysql", e)