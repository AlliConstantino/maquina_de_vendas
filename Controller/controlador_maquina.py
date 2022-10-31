from Controller.controlador_administrador import ControladorAdministrador
from Controller.controlador_produto import ControladorProduto
from View.tela_maq import TelaMaquina
from View.tela_gerencia import TelaGerencia


class ControladorMaquina:
    def __init__(self):
        self.__administradores = []
        self.__produtos = []
        self.__historico = []
        self.__controlador_adm = ControladorAdministrador(self)
        self.__controlador_prod = ControladorProduto(self)
        self.__tela_maq = TelaMaquina()
        self.__tela_gerencia = TelaGerencia()

    @property
    def administradores(self):
        return self.__administradores

    @property
    def produtos(self):
        return self.__produtos

    @property
    def historico(self):
        return self.__historico

    def opcoes_maquina(self):
        while True:
            x = self.__tela_maq.opcoes_maq()
            if x == 1:
                pass  # self.vendas()
            elif x == 2:
                self.opcoes_gerencia()
            elif x == 0:
                self.__tela_maq.mostra_msg('Até logo!')
                break

    def opcoes_gerencia(self):
        a = self.__tela_gerencia.logar()
        for i in self.__administradores:
            if i.codigo == a['codigo'] and i.senha == a['senha']:
                while True:
                    x = self.__tela_gerencia.opcoes_gerencia()
                    if x == 1:
                        self.__controlador_prod.opcoes_produto()
                    elif x == 2:
                        self.__controlador_adm.opcoes_administrador()
                    elif x == 0:
                        break
                break
        else:
            self.__tela_gerencia.mostra_msg('Dados incorretos')

    def iniciar(self):
        self.opcoes_maquina()


'''
    def vendas(self):
        while True:
            self.__controlador_prod.listar_produtos()
            self.__tela_maq.mostra_msg('Insira o código do produto')
            cod = self.__tela_maq.pega_codigo()
            if cod == 999:
                break
            else:
                for i in self.__produtos:
                    if i.codigo == cod:
                        i.quantidade -= 1
'''
