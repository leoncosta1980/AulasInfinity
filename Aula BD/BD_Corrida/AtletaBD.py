from mysql.connector import Error

class AtletaBD:
    def __init__(self, banco):
        self.banco = banco

    def listaAtletas(self):
        try:
            sql="SELECT * FROM atleta"
            resultados = self.banco.cursor()
            resultados.execute(sql)
            return resultados
        except Error as e:
            print ("Erro ao obter lista de atletas. ", e)
            
    def insereAtletas (self, atleta):
        try:
            sql = "INSERT INTO atleta (nome, idade) VALUES (%s, %s)"
            resultados = self.banco.cursor()
            resultados.execute(sql, (atleta.nome, atleta.idade))
            self.banco.commit()
            return resultados
        except Error as e:
            print("Erro ao inserir atleta. ", e)