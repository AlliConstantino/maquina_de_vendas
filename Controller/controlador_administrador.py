from Model.administrador import Administrador
from View.tela_administrador import TelaAdministrador


class ControladorAdministrador:
    def __init__(self, controlador_maquina):
        self.__tela_adm = TelaAdministrador()
        self.__controlador_maq = controlador_maquina

    def novo_administrador(self):
        dados_adm = self.__tela_adm.novo_adm()
        adm = Administrador(dados_adm['nome'],
                            dados_adm['codigo'],
                            dados_adm['senha'])
        if adm not in self.__controlador_maq.administradores:
            self.__controlador_maq.administradores.append(adm)

    def listar_administradores(self):
        if len(self.__controlador_maq.administradores) == 0:
            self.__tela_adm.mostra_msg('Lista vazia.')
        else:
            for adm in self.__controlador_maq.administradores:
                self.__tela_adm.mostra_adm(adm.nome, adm.codigo)
