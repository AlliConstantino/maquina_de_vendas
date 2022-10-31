from Model.comida import Comida
from View.tela_comida import TelaComida


class ControladorComida:
    def __init__(self, controlador_maquina):
        self.__tela_comida = TelaComida() #cria uma nova tela
        self.__controlador_maquina = controlador_maquina

    def opcoes_comida(self):
        while True:
            op = self.__tela_comida.opcoes_comida()
            if op == 1:
                self.nova_comida()
            elif op == 2:
                self.excluir_comida()
            elif op == 3:
                self.listar_comidas()

            elif op == 4:
                self.alterar_comida()
            elif op == 0:
                break

    def nova_comida(self):
        dados_comida = self.__tela_comida.novo_comida()
        nova_comida = Comida(dados_comida['nome'],dados_comida['codigo'],dados_comida['tipo'], dados_comida['quantidade'], dados_comida['tipo'])
        for comida in self.__controlador_maquina.comida:
            if comida.codigo == nova_comida.codigo:
                self.__tela_comida.mostra_msg('comida já existe!')
                self.opcoes_comida()
        else:
            self.__controlador_maquina.comida.append(nova_comida)
            self.opcoes_comida()

    def excluir_comida(self):
        cod = self.__tela_comida.pega_codigo()
        for comida in self.__controlador_maquina.comidas:
            if comida.codigo == cod:
                self.__controlador_maquina.comida.remove(comida)
                self.listar_comidas()

    def listar_comidas(self):
        if len(self.__controlador_maquina.comidas) == 0:
            self.__tela_comida.mostra_msg('Lista  de bebidas esta vazia :( ')
        else:
            for comida in self.__controlador_maquina.comidas:
                self.__tela_comida.mostra_comida(comida.nome, comida.codigo, comida.preco, comida.quantidade, comida.tipo)
