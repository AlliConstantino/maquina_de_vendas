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
            elif op == 4:
                self.alterar_adm()
            elif op == 0:
                break

    def novo_administrador(self):
        dados_adm = self.__tela_adm.novo_adm()
        novo_adm = Administrador(dados_adm['nome'],
                                 dados_adm['codigo'],
                                 dados_adm['senha'])
        flag = False
        for admin in self.__controlador_maq.administradores:
            if admin.codigo == novo_adm.codigo:
                self.__tela_adm.mostra_msg('Administrador já existe!')
                flag = True
        if flag is False:
            self.__controlador_maq.administradores.append(novo_adm)

    def excluir_administrador(self):
        if len(self.__controlador_maq.administradores) >= 1:
            self.listar_administradores()
            cod = self.__tela_adm.pega_codigo()
            flag = True
            for adm in self.__controlador_maq.administradores:
                if adm.codigo == cod:
                    self.__controlador_maq.administradores.remove(adm)
                    flag = False
            if flag is True:
                self.__tela_adm.mostra_msg('Administrador não encontrado!')
        else:
            self.__tela_adm.mostra_msg('Lista vazia.')

    def listar_administradores(self):
        if len(self.__controlador_maq.administradores) == 0:
            self.__tela_adm.mostra_msg('Lista vazia.')
        else:
            for adm in self.__controlador_maq.administradores:
                self.__tela_adm.mostra_adm(adm.nome, adm.codigo)

    def alterar_adm(self):
        self.__tela_adm.mostra_msg('Quem deseja alterar?')
        self.listar_administradores()
        cod = self.__tela_adm.pega_codigo()
        flag = False
        for adm in self.__controlador_maq.administradores:
            if adm.codigo == cod:
                novos_dados = self.__tela_adm.pega_dados()
                adm.codigo = novos_dados['codigo']
                adm.nome = novos_dados['nome']
                adm.senha = novos_dados['senha']
                flag = True
        if flag is False:
            self.__tela_adm.mostra_msg('Código inexistente.')
