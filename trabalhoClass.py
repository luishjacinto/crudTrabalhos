import datetime
import decimal
from autorClass import Autor
from autorDao import AutorDao

autorDao = AutorDao()

class Trabalho:

    def __init__(self, conteudo, nota, dataEntrega, titulo):
        self._conteudo = conteudo
        self._nota = nota
        self._dataEntrega = dataEntrega
        self._titulo = titulo
        self._dataHoraAtualizacao = datetime.datetime.now()
        self._autor = []

    def _get_cod(self):
        return self._cod
    def _get_conteudo(self):
        return self._conteudo 
    def _get_dataEntrega(self):
        return self._dataEntrega
    def _get_nota(self):
        return self._nota
    def _get_titulo(self):
        return self._titulo
    def _get_dataHoraAtualizacao(self):
            return self._dataHoraAtualizacao
    def _get_autor(self):
            return self._autor


    def _set_cod(self, cod):
        self._cod = cod
    def _set_conteudo(self, conteudo):
        self._conteudo = conteudo
    def _set_dataEntrega(self, dataEntrega):
        self._dataEntrega = dataEntrega    
    def _set_nota(self, nota):
        self._nota = nota
    def _set_titulo(self, titulo):
        self._titulo = titulo
    def _set_dataHoraAtualizacao(self, dataHoraAtualizacao):
        self._dataHoraAtualizacao =  dataHoraAtualizacao
    def _set_autor(self, autor):
        self._autor = autor

    
    def __str__(self):
        listaAutores = ''
        for i in range(0, len(self._autor)):
            listaAutores += str(self._autor[i])
            
        return '{\nCódigo: ' + str(self._cod) + '\nConteudo: ' + self._conteudo + '\nData de Entrega: ' + str(self._dataEntrega) + '\nNota: ' + str(self._nota) + '\nTitulo:' + self._titulo + '\nData e Hora de Atualização: ' + str(self._dataHoraAtualizacao) + '\nAutor(es): [' + listaAutores + ']\n}'

    cod = property(_get_cod,_set_cod)
    conteudo = property(_get_conteudo,_set_conteudo)
    dataEntrega = property(_get_dataEntrega,_set_dataEntrega)
    nota = property(_get_nota,_set_nota)
    titulo = property(_get_titulo,_set_titulo)
    dataHoraAtualizacao = property(_get_dataHoraAtualizacao,_set_dataHoraAtualizacao)
    autor = property(_get_autor,_set_autor)

