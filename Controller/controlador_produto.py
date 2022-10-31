from Model.produto import Produto
from View.tela_produto import TelaProduto


class ControladorProduto:
    def __init__(self, controlador_maquina):
        self.__tela_produto = TelaProduto() #cria uma nova tela
        self.__controlador_maquina = controlador_maquina

    def opcoes_produto(self):
        while True:
            op = self.__tela_produto.opcoes_produto()
            if op == 1:
                self.novo_produto()
            elif op == 2:
                self.excluir_produto()
            elif op == 3:
                self.listar_produtos()

            elif op == 4:
                self.alterar_produto()
            elif op == 0:
                break

    def novo_produto(self):
        dados_produto = self.__tela_produto.novo_produto()
        novo_produto = Produto(dados_produto['nome'],dados_produto['codigo'], dados_produto['preco'],
                               dados_produto['quantidade'], dados_produto['tipo'])
        for produto in self.__controlador_maquina.produtos:
            if produto.codigo == novo_produto.codigo:
                self.__tela_produto.mostra_msg('Produto já existe!')
                self.opcoes_produto()
        else:
            self.__controlador_maquina.produtos.append(novo_produto)
            self.opcoes_produto()

    def excluir_produto(self):
        cod = self.__tela_produto.pega_codigo()
        for produto in self.__controlador_maquina.produtos:
            if produto.codigo == cod:
                self.__controlador_maquina.produtos.remove(produto)
                self.listar_produtos()

    def listar_produtos(self):
        if len(self.__controlador_maquina.produtos) == 0:
            self.__tela_produto.mostra_msg('Lista  de produtos esta vazia :(.')
        else:
            for produto in self.__controlador_maquina.produtos:
                self.__tela_produto.mostra_produto(produto.nome, produto.codigo, produto.preco, produto.quantidade, produto.tipo)
