from Controller.controlador_administrador import ControladorAdministrador
from Controller.controlador_produto import ControladorProduto
from GUI_View.tela_maquina import TelaMaquina
from GUI_View.tela_gerencia import TelaGerencia


class ControladorMaquina:
    def __init__(self):
        self.__produtos = []
        self.__historico = []
        self.__controlador_adm = ControladorAdministrador(self)
        self.__controlador_prod = ControladorProduto(self)
        self.__tela_maq = TelaMaquina()
        self.__tela_gerencia = TelaGerencia()

    @property
    def produtos(self):
        return self.__produtos

    @property
    def historico(self):
        return self.__historico

    def opcoes_maquina(self):
        while True:
            try:
                x = self.__tela_maq.opcoes_maquina()
                if x is None:
                    return None
                if x == 0:
                    return None
                # if x == 1:
                #    self.vendas()
                elif x == 2:
                    self.opcoes_gerencia()
                elif x == 0:
                    self.__tela_maq.mostra_mensagem('Encerrando máquina!', 'Até logo!')
                    break
            except TypeError:
                pass

    def opcoes_gerencia(self):
        codigo, senha = self.__tela_gerencia.logar()
        if codigo is None or senha is None:
            return None
        for i in self.__controlador_adm.administradores.values():
            if i.codigo == codigo and i.senha == senha:
                while True:  # Permanece na tela da máquina
                    op = self.__tela_gerencia.opcoes_gerencia()
                    if op is None:
                        return None
                    if op == 0:
                        return None
                    if op == 1:
                        self.__controlador_prod.opcoes_produto()
                    elif op == 2:
                        self.__controlador_adm.opcoes_administrador()
        else:
            self.__tela_gerencia.mostra_mensagem('Erro', 'Dados incorretos')

    def iniciar(self):
        try:
            self.opcoes_maquina()
        except KeyboardInterrupt:
            print('Obrigado!!!')


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
                        self.__tela_maq.mostra_msg('Muito obrigado!')
                        break
'''