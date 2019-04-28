import psycopg2
from autorClass import Autor
from abstractDao import AbstractDao

class AutorDao(AbstractDao):
    def __init__(self):
        pass

    def inserir(self, autor):
        conn = self.conectar()
        try:
            with conn.cursor() as cur:
                cur.execute("""INSERT INTO "Autor" (nome, email) 
                VALUES (%s, %s)""", [autor._nome, autor._email])

                conn.commit()
                cur.close()
                conn.close()
                print("INSERT realizado!")
        except:
            print("Erro ao executar INSERT")


    def buscar(self, cod):
        conn = self.conectar()
        try:
            with conn.cursor() as cur:
                cur.execute("""SELECT * FROM "Autor" WHERE cod=%s""", [cod])

                r = cur.fetchall()
                a = Autor(r[0][1], r[0][2])
                a.cod = r[0][0]
                cur.close()
                return a
        except:
            print("Erro ao executar SELECT")

    def listar(self):
        conn = self.conectar()
        try:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM "Autor"') 
                
                r = cur.fetchall()
                lista= []
                for i in range(0, len(r)):
                    a = Autor(r[i][1], r[i][2])
                    a.cod = r[i][0]
                    lista.append(a)
                cur.close()
                return lista
        except:
            print("Erro ao executar SELECT")
   
    def editar(self, autor):
        conn = self.conectar()
        try:
            with conn.cursor() as cur:
                cur.execute("""UPDATE "Autor" SET nome = %s , email = %s 
                WHERE cod = %s""", [autor._nome, autor._email, autor._cod])
                conn.commit()
                cur.close()
                print("UPDATE realizado!")
        except:
            print("Erro ao executar UPDATE")
    
    def deletar(self, cod):
        conn = self.conectar()
        try:
            with conn.cursor() as cur:
                cur.execute("""DELETE FROM "Autor" WHERE cod=%s""", [cod] )
                conn.commit()
                cur.close()
                conn.close()
                print("DELETE realizado!")
        except:
            print("Erro ao executar DELETE")