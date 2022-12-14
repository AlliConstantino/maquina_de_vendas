class Administrador:
    def __init__(self, nome, codigo, senha):
        self.__nome = nome
        self.__codigo = codigo
        self.__senha = senha

    @property
    def nome(self):
        return self.__nome

    @property
    def codigo(self):
        return self.__codigo

    @property
    def senha(self):
        return self.__senha

    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome

    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo

    @senha.setter
    def senha(self, senha):
        if isinstance(senha, str):
            self.__senha = senha
