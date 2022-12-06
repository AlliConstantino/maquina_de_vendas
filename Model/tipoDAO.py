from dao import DAO
from tipo import Tipo

class TipoDAO(DAO):
    def __int__(self):
        super().__int__('tipo.pkl')

    def __add__(self, tipo:Tipo):
        if (isinstance(tipo, Tipo)) and (tipo is not None) :
            super().__add(tipo, Tipo)

    def get(self, key: int):
        if isinstance(key,int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key,int):
            return super().remove(key)