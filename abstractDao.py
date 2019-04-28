import psycopg2

class AbstractDao:  

    def conectar(self):
        return psycopg2.connect('host=localhost port=5432 dbname=trabalhoDS2 user=postgres password=postgres')

    def inserir(self,object):
        pass

    def buscar(self,cod):
        pass

    def listar(self):
        pass

    def editar(self, object):
        pass

    def deletar(self, cod):
        pass
    