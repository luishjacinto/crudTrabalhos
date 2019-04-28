import psycopg2
import datetime
from autorClass import Autor
from autorDao import AutorDao
from trabalhoClass import Trabalho
from abstractDao import AbstractDao

class TrabalhoDao(AbstractDao):
    
    def inserir(self, trabalho, autoresCod):
        conn = self.conectar()
        try:
            with conn.cursor() as cur:
                cur.execute("""INSERT INTO "Trabalho" (conteudo, nota, "dataEntrega", titulo) 
                VALUES (%s, %s, %s, %s)""", [trabalho._conteudo, trabalho._nota, trabalho._dataEntrega, trabalho._titulo])
                conn.commit()

                for i in range(0, len(autoresCod)):
                    cur.execute('SELECT * FROM "Trabalho" ORDER BY cod DESC')
                    cod = cur.fetchall()[0][0]
                    cur.execute("""INSERT INTO "TrabalhoAutor" ("codAutor","codTrabalho") VALUES (%s,%s)""",[autoresCod[i], cod])
                    conn.commit()

                cur.close()
                conn.close()
                print("INSERT realizado!")
        except:
            print("Erro ao executar INSERT")
       
    def buscar(self, cod):
        conn = self.conectar()
        cur = conn.cursor()
        try:
            with conn.cursor() as cur:
                cur.execute("""SELECT * FROM "Trabalho" WHERE cod=%s""", [cod] )
                r = cur.fetchall()
                t = Trabalho(r[0][1], r[0][2], r[0][3], r[0][4])
                t.cod = r[0][0]

                cur.execute("""SELECT * FROM "TrabalhoAutor" WHERE "codTrabalho"=%s""", [cod] )
                r1 = cur.fetchall()
                autores = []
                autorDao = AutorDao()
                for i in range(0, len(r1)):
                    autores.append(autorDao.buscar(r1[i][0]))
                    
                t.autor = autores

                cur.close()
                return t
        except:
           print("Erro ao executar SELECT")

    def listar(self):
        conn = self.conectar()
        try:
            with conn.cursor() as cur:
                cur.execute('SELECT * FROM "Trabalho"') 

                r = cur.fetchall()
                lista= []
                for i in range(0, len(r)):
                    t = Trabalho(r[i][1], r[i][2], r[i][3], r[i][4])
                    t.cod = r[i][0]

                    cur.execute("""SELECT * FROM "TrabalhoAutor" WHERE "codTrabalho"=%s""", [t.cod] )
                    r1 = cur.fetchall()
                    autores = []
                    autorDao = AutorDao()
                    for i in range(0, len(r1)):
                        autores.append(autorDao.buscar(r1[i][0]))

                    t.autor = autores

                lista.append(t)

                cur.close()
                return lista
        except:
            print("Erro ao executar SELECT")
   
    def editar(self, trabalho):
        conn = self.conectar()
        try:
            with conn.cursor() as cur:
                cur.execute("""UPDATE "Trabalho" SET conteudo = %s , nota = %s , "dataEntrega" = %s
                , titulo = %s , "dataHoraAtualizacao" = %s  WHERE cod = %s""", 
                [trabalho._conteudo, trabalho._nota, trabalho._dataEntrega, trabalho._titulo,
                datetime.datetime.now(), trabalho._cod])

                conn.commit()
                cur.close()
                print("UPDATE realizado!")
        except:
            print("Erro ao executar UPDATE")
    
    def deletar(self, cod):
        conn = self.conectar()
        try:
            with conn.cursor() as cur:
                cur.execute("""DELETE FROM "Trabalho" WHERE cod=%s""", [cod] )
                conn.commit()
                cur.close()
                conn.close()
                print("DELETE realizado!")
        except:
            print("Erro ao executar DELETE")