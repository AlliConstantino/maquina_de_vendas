from Model.produto import Produto
from View.tela_produto import TelaProduto


class ControladorProduto:
    def __init__(self, controlador_maquina):
        self.__tela_produto = TelaProduto()
        self.__controlador_maquina = controlador_maquina
        #self.__produto = Produto

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
        novo_produto = Produto(dados_produto['nome'], dados_produto['codigo'], dados_produto['preco'],
                               dados_produto['quantidade'], dados_produto['tipo'])
        for produto in self.__controlador_maquina.produtos:
            if produto.codigo == novo_produto.codigo:
                self.__tela_produto.mostra_msg('Produto já existe!')
                break
        else:
            self.__controlador_maquina.produtos.append(novo_produto)

    def excluir_produto(self):
        cod = self.__tela_produto.pega_codigo()
        for produto in self.__controlador_maquina.produtos:
            if produto.codigo == cod:
                self.__controlador_maquina.produtos.remove(produto)
                break
        else:
            self.__tela_produto.mostra_msg('Produto não encontrado.')

    def listar_produtos(self):
        if len(self.__controlador_maquina.produtos) == 0:
            self.__tela_produto.mostra_msg('Não há produtos na máquina!')
        else:
            for produto in self.__controlador_maquina.produtos:
                self.__tela_produto.mostra_produto(produto.nome, produto.codigo, produto.preco, produto.quantidade, produto.tipo)

    def alterar_produto(self):
        self.__tela_produto.mostra_msg('O que deseja alterar?')
        self.listar_produtos()
        cod = self.__tela_produto.pega_codigo()
        dados = self.__tela_produto.pega_dados()
        for produto in self.__controlador_maquina.produtos:
            if produto.codigo == cod:
                produto.nome = dados['nome']
                produto.codigo = dados['codigo']
                produto.preco = dados['preco']
                produto.quantidade = dados['quantidade']
                produto.tipo = dados['tipo']
                break
        else:
            self.__tela_produto.mostra_msg('Produto não encontrado.')
