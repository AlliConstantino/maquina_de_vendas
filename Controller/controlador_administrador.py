from Model.administrador import Administrador
from View.tela_administrador import TelaAdministrador


class ControladorAdministrador:
    def __init__(self, controlador_maquina):
        self.__tela_adm = TelaAdministrador()
        self.__controlador_maq = controlador_maquina

    def opcoes_administrador(self):
        while True:
            op = self.__tela_adm.opcoes_administrador()
            if op == 1:
                self.novo_administrador()
            elif op == 2:
                self.excluir_administrador()
            elif op == 3:
                self.listar_administradores()
            elif op == 0:
                break

    def novo_administrador(self):
        dados_adm = self.__tela_adm.novo_adm()
        novo_adm = Administrador(dados_adm['nome'],
                                 dados_adm['codigo'],
                                 dados_adm['senha'])
        for admin in self.__controlador_maq.administradores:
            if admin.codigo == novo_adm.codigo:
                self.__tela_adm.mostra_msg('Administrador já existe!')
                self.opcoes_administrador()
        else:
            self.__controlador_maq.administradores.append(novo_adm)
            self.opcoes_administrador()

    def excluir_administrador(self):
        cod = self.__tela_adm.pega_codigo()
        for adm in self.__controlador_maq.administradores:
            if adm.codigo == cod:
                self.__controlador_maq.administradores.remove(adm)
                self.listar_administradores()

    def listar_administradores(self):
        if len(self.__controlador_maq.administradores) == 0:
            self.__tela_adm.mostra_msg('Lista vazia.')
        else:
            for adm in self.__controlador_maq.administradores:
                self.__tela_adm.mostra_adm(adm.nome, adm.codigo)
