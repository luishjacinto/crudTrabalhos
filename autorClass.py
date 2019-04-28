class Autor:
    
    def __init__(self, nome, email):
        self._nome = str(nome).strip()
        self._email = str(email).strip()

    def _get_cod(self):
        return self._cod
    def _get_nome(self):
        return self._nome
    def _get_email(self):
        return self._email

    def _set_cod(self, cod):
        self._cod = cod
    def _set_nome(self, nome):
        self._nome = nome
    def _set_email(self, email):
        self._email = email


    def __str__(self):
        return '{\nCódigo: ' + str(self._cod) + '\nNome: ' + self._nome + '\nE-mail: ' + self._email + '\n}'

    cod = property(_get_cod,_set_cod)
    nome = property(_get_nome,_set_nome)
    autor = property(_get_email,_set_email)
