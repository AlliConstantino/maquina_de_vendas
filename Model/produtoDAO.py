from dao import DAO
from produto import Produto

class ProdutoDAO(DAO):
    def __int__(self):
        super().__int__('produtos.pkl')

    def __add__(self, produto:Produto):
        if (isinstance(produto.codigo, int)) and (produto is not None) and isinstance(produto, Produto):
            super().__add(produto.codigo, produto)

    def get(self, key: int):
        if isinstance(key,int):
            return super().get(key)

    def remove(self, key: int):
        if isinstance(key,int):
            return super().remove(key)