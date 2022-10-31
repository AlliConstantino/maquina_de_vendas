from Model.bebida import Bebida
from View.tela_bebida import TelaBebida


class ControladorBebida:
    def __init__(self, controlador_bebida):
        self.__tela_bebida = TelaBebida() #cria uma nova tela
        self.__controlador_bebida = controlador_bebida

    def opcoes_administrador_bebida(self):
        while True:
            op = self.__tela_bebida.opcoes_bebida()
            if op == 1:
                self.nova_bebida()
            elif op == 2:
                self.excluir_bebida()
            elif op == 3:
                self.listar_bebidas()

            elif op == 4:
                self.alterar_bebida()
            elif op == 0:
                break

    def nova_bebida(self):
        dados_bebida = self.__tela_bebida.novo_bebida()
        nova_bebida = Bebida(dados_bebida['nome'],dados_bebida['codigo'],dados_bebida['tipo'], dados_bebida['quantidade'])
        for bebida in self.__controlador_bebida.bebida:
            if bebida.codigo == nova_bebida.codigo:
                self.__tela_bebida.mostra_msg('Bebida já existe!')
                self.__tela_bebida.opcoes_bebida()
        else:
            self.__controlador_bebida.bebidas.append(nova_bebida)
            self.opcoes_administrador_bebida()

    def excluir_bebida(self):
        cod = self.__tela_bebida.pega_codigo()
        for bebida in self.__controlador_bebida.bebidas:
            if bebida.codigo == cod:
                self.__controlador_bebida.bebida.remove(bebida)
                self.listar_bebida()

    def listar_bebidas(self):
        if len(self.__controlador_bebida.bebidas) == 0:
            self.__tela_bebida.mostra_msg('Lista  de bebidas esta vazia :( ')
        else:
            for bebida in self.__controlador_bebida.bebidas:
                self.__tela_bebida.mostra_bebida(bebida.nome, bebida.codigo, bebida.preco, bebida.quantidade, bebida.tipo)
