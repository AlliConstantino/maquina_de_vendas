class Produto:
    def __int__(self,nome: str, codigo, preco: float , quantidade: int):
        self.__nome = nome
        self.__codigo = codigo
        self.__quantidade = quantidade


        @property
        def nome(self):
            return self.__nome

        @property
        def codigo(self):
            return self.__codigo

        @property
        def preco(self):
            return self.__preco

        @property
        def quantidade(self):
            return self.__quantidade

        #setters

        @nome.setter
        def nome(self, nome:str):
            self.__nome = nome

        @codigo.setter
        def codigo(self, codigo):
            self.__codigo = codigo

        @preco.setter
        def preco(self, preco: float):
            self.__preco = preco

        @quantidade.setter
        def quantidade(self, quantidade: int):
            self.__quantidade = quantidade
