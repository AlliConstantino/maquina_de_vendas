from Model.administrador import Administrador
from GUI_View.tela_adm import TelaAdm
from Exception.AdmDuplicadoException import AdmDuplicadoException
from DAO.administrador_dao import AdministradorDao


class ControladorAdministrador:
    def __init__(self, controlador_maquina):
        self.__tela_adm = TelaAdm()
        self.__administradores = AdministradorDao()
        self.__controlador_maq = controlador_maquina
        padrao = Administrador('Admin', 999, '0000')
        if padrao.codigo not in self.administradores.keys():
            self.__administradores.add(padrao.codigo, padrao)

    @property
    def administradores(self):
        return self.__administradores.cache

    def opcoes_administrador(self):
        while True:
            op = self.__tela_adm.opcoes_adm()
            if op == 1:
                self.novo_administrador()
            elif op == 2:
                self.excluir_administrador()
            elif op == 3:
                self.alterar_adm()
            elif op == 0:
                return
            elif op is None:
                return

    def novo_administrador(self):
        dados_adm = self.__tela_adm.dados_adm()  # Busca os dados para o novo adm
        if dados_adm is None:
            return
        elif len(dados_adm[1]['it_nome']) == 0 or len(dados_adm[1]['it_senha']) == 0:  # Verifica campos vazios
            self.__tela_adm.mostra_mensagem('Campos vazios', 'Alguns campos não foram preenchidos!')
        elif dados_adm[0] == 0:
            return
        elif dados_adm[0] == 1:
            novo_adm = Administrador(dados_adm[1]['it_nome'],
                                     dados_adm[1]['it_codigo'],
                                     dados_adm[1]['it_senha'])
            try:
                for i in self.administradores.values():  # Percorre os administradores verificando se já existe o código
                    if i.codigo == novo_adm.codigo:
                        raise AdmDuplicadoException
            except AdmDuplicadoException:
                self.__tela_adm.mostra_mensagem('Administrador duplicado',
                                                'Já existe um administrador com o mesmo código')
                return
            else:
                self.__administradores.add(novo_adm.codigo, novo_adm)

    def excluir_administrador(self):
        admins = []
        for i in self.administradores.values():
            admins.append(i)
        op = self.__tela_adm.excluir_adm(admins)  # Envia a lista necessária para a listbox da tela
        if op is None:
            return
        elif op[0] == 0:
            return
        else:
            try:
                codigo = (op[1]['lb_adm_exc'][0][1])  # Pegando código do dicionário
                if len(self.administradores) == 1:
                    self.__tela_adm.mostra_mensagem('Impossível excluir administrador',
                                                    'É necessário haver ao menos um administrador na máquina')
                else:
                    for i in self.administradores.values():
                        if i.codigo == codigo:
                            self.__administradores.remove(codigo)
                            self.__tela_adm.mostra_mensagem('Concluído', 'Administrador excluído com sucesso!')
            except IndexError:
                return
            except TypeError:
                return
            except RuntimeError:
                pass

    def alterar_adm(self):
        admins = []
        for i in self.administradores.values():
            admins.append(i)
        res = self.__tela_adm.alterar_administrador(admins)  # Pega o adm a ser alterado, passando lista pra listbox
        if res is None:
            return
        if res[0] == 0:
            return
        else:
            try:
                cod = res[1]['lb_adm_alt'][0][1]
                op = self.__tela_adm.opcoes_alteracao()
                if op is None:
                    return
                elif op[0] == 0 or op[0] is None:
                    return
                elif op[0] == 1 and len(op[1]) == 0:
                    return
                else:
                    x = self.__tela_adm.alteracao()
                    if x is None:
                        return
                    if x[0] == 0:
                        return
                    if x[0] is None:
                        return
                    if x[1]['it_alter'] is None:
                        return
                    for i in self.administradores.values():
                        if i.codigo == cod:
                            if op[0] == 2:
                                i.nome = x[1]['it_alter']
                                self.__tela_adm.mostra_mensagem('Sucesso', 'Nome alterado')
                                self.__administradores.update()
                                return
                            elif op[0] == 3:
                                i.codigo = int(x[1]['it_alter'])
                                self.__tela_adm.mostra_mensagem('Sucesso', 'Código alterado')
                                self.__administradores.update()
                                return
                            elif op[0] == 4:
                                self.__tela_adm.mostra_mensagem('Sucesso', 'Senha alterada')
                                i.senha = x[1]['it_alter']
                                self.__administradores.update()
                                return

            except IndexError:
                return
            except TypeError:
                return
            except ValueError:
                self.__tela_adm.mostra_mensagem('Código inválido!', 'Somente números inteiros são aceitos')
                return
            except RuntimeError:
                pass
