import datetime
from autorClass import Autor
from autorDao import AutorDao
from trabalhoClass import Trabalho
from trabalhoDao import TrabalhoDao

autorDao = AutorDao()
trabalhoDao = TrabalhoDao()
"""
#Autores
print('TESTE AUTORES')
#cod 1
autor1 = Autor('Altair', 'Ac@brotherhood.com')
autorDao.inserir(autor1)

#cod 2
autor2 = Autor('Master Chief', 'cortana@halo.com')
autorDao.inserir(autor2)

print('TESTE BUSCA')
print(autorDao.buscar(1))

autor3 = autorDao.buscar(1)
autor3._nome = 'Ezio'
autorDao.editar(autor3)

print('TESTE EDICAO')
print(autorDao.buscar(1))

lista = autorDao.listar()

print('TESTE LISTA')
for i in range(0,len(lista)):
    print(lista[i])

autorDao.deletar(1)

print('TESTE LISTA DPS DA EXCLUSÃO')
lista = autorDao.listar()
for i in range(0,len(lista)):
    print(lista[i])

#Trabalhos
print('TESTE Trabalhos')
#cod 1
trabalho1 = Trabalho('Jack Sparrow é foda', 10, datetime.datetime(2018, 5, 20), 'Piratas do Caribe')
trabalhoDao.inserir(trabalho1,[2])

#cod 2
trabalho2 = Trabalho('INSERT INTO', 2, datetime.datetime(2018, 5, 18), 'DS2')
trabalhoDao.inserir(trabalho2,[1,2])
"""
print('TESTE BUSCA')
print(trabalhoDao.buscar(2))
"""
trabalho3 = trabalhoDao.buscar(2)
trabalho3.conteudo = 'Conteudo ALTER'
trabalhoDao.editar(trabalho3)

print('TESTE EDICAO')
print(trabalhoDao.buscar(2))

listaTrab = trabalhoDao.listar()

print('TESTE LISTA')
for i in range(0,len(listaTrab)):
    print(listaTrab[i])

trabalhoDao.deletar(1)

print('TESTE LISTA DPS DA EXCLUSÃO')
listaTrab = trabalhoDao.listar()
for i in range(0,len(listaTrab)):
    print(listaTrab[i])
"""