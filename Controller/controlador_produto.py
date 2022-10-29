from Model.produto import Produto
from View.tela_produto import TelaProduto


class ControladorProduto:
    def __init__(self, controlador_produto):
        self.__tela_produto = Telaproduto() #cria uma nova tela
        self.__controlador_produto = controlador_produto

    # Coloca o nome só como opcoes_produto

    def opcoes_administrador_produto(self):
        while True:
            op = self.__tela_produto.opcoes_produto()
            if op == 1:
                self.novo_produto()
            elif op == 2:
                self.excluir_produto()
            elif op == 3:
                self.listar_produto()

            elif op == 4:
                self.alterar_produto()
            elif op == 0:
                break

    def novo_produto(self):
        dados_produto = self.__tela_produto.novo_produto()
        novo_produto = Produto(dados_produto['nome'],dados_produto['codigo'],dados_produto['tipo'], dados_produto['quantidade'])
        for produto in self.__controlador_produto.produtos:
            if produto.codigo == novo_produto.codigo:
                self.__tela_produto.mostra_msg('Produto já existe!')
                self.opcoes_produto()
        else:
            self.__controlador_produto.produtos.append(novo_produto)
            self.opcoes_administrador_produto()

    def excluir_produto(self):
        cod = self.__tela_produto.pega_codigo()
        for produto in self.__controlador_produto.produtos:
            if produto.codigo == cod:
                self.__controlador_produto.produto.remove(produto)
                self.listar_produtos()

    def listar_produtos(self):
        if len(self.__controlador_produto.produtos) == 0:
            self.__tela_produto.mostra_msg('Lista  de produtos esta vazia :(.')
        else:
            for produto in self.__controlador_produto.produtos:
                self.__tela_produto.mostra_produto(produto.nome, produto.codigo, produto.preco, produto.quantidade, produto.tipo)
