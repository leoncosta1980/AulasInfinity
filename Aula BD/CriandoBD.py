import mysql.connector
from mysql.connector import Error

try:
    connector = mysql.connector.connect(
        host='localhost',
        user='root',
        password='aluno99'
    )
    
    db_info = connector.get_server_info()
    print("Conectou ao mysql versão: ", db_info)
    
    cursor = connector.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS aula21082021")
    cursor.execute("CREATE TABLE IF NOT EXISTS aula21082021.STUDENTS (REGISTRATION INT AUTO_INCREMENT, NAME VARCHAR(30), PRIMARY KEY (REGISTRATION))")
    cursor.execute("ALTER TABLE aula21082021.STUDENTS ADD COLUMN (GENDER VARCHAR(1))")
    
except Error as e:
    print("Erro ao acessar o mysql: ",e)
