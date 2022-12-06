from abc import ABC, abstractmethod


class DAO(ABC):
    @abstractmethod
    def __int__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __add__(self, key, obj):
        self.__cache[key] = obj
        self.__dump()

    def remove(self, key):
        try:
            return self.__cache[key]
        except KeyError:
            #colocar excecao aqui
            for i in self.get_all():
                if i.codigo == key:
                    self.__cache.remove(i)
                    self.__dump() #pra jogar fora de vez
            else:
                print("Não foi possivel remover, tente novamente")

    def get_all(self):
        return self.__cache.values()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource, rb))