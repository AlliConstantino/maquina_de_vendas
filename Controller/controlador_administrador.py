from Model.administrador import Administrador
from GUI_View.tela_adm import TelaAdm
from Exception.AdmDuplicadoException import AdmDuplicadoException


class ControladorAdministrador:
    def __init__(self, controlador_maquina):
        self.__tela_adm = TelaAdm()
        self.__controlador_maq = controlador_maquina
        self.__controlador_maq.administradores.append(Administrador('Admin', 999, '0000'))

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
                break
            elif op is None:
                break

    def novo_administrador(self):
        dados_adm = self.__tela_adm.dados_adm()
        if dados_adm is None:
            return
        elif dados_adm[0] == 0:
            return
        elif dados_adm[0] == 1:
            novo_adm = Administrador(dados_adm[1]['it_nome'],
                                     dados_adm[1]['it_codigo'],
                                     dados_adm[1]['it_senha'])
            try:
                for admin in self.__controlador_maq.administradores:
                    if admin.codigo == dados_adm[1]['it_codigo']:
                        raise AdmDuplicadoException
            except AdmDuplicadoException:
                self.__tela_adm.mostra_mensagem('Administrador duplicado',
                                                'Já existe um administrador com o mesmo código')
                return
            else:
                self.__controlador_maq.administradores.append(novo_adm)

    def excluir_administrador(self):
        op = self.__tela_adm.excluir_adm(self.__controlador_maq.administradores)
        if op is None:
            return
        elif op[0] == 0:
            print(op[0])
            return
        else:
            try:
                codigo = (op[1]['lb_adm_exc'][0][1])
                if len(self.__controlador_maq.administradores) == 1:
                    self.__tela_adm.mostra_mensagem('Impossível excluir administrador',
                                                    'É necessário haver ao menos um administrador na máquina')
                else:
                    for i in self.__controlador_maq.administradores:
                        if i.codigo == codigo:
                            self.__controlador_maq.administradores.remove(i)
                            self.__tela_adm.mostra_mensagem('Concluído', 'Administrador excluído com sucesso!')
            except IndexError:
                return
            except TypeError:
                return

    def alterar_adm(self):
        res = self.__tela_adm.alterar_administrador(self.__controlador_maq.administradores)
        try:
            cod = res[1]['lb_adm_alt'][0][1]
            if res is None:
                return
            if res[0] == 0:
                return
            else:
                op = self.__tela_adm.opcoes_alteracao()
                x = self.__tela_adm.alteracao()
                if op is None or x is None:
                    return
                if op[0] == 0 or x[0] == 0:
                    return
                for i in self.__controlador_maq.administradores:
                    if i.codigo == cod:
                        if op[0] == 2:
                            i.nome = x[0]['it_alter'][0][1]
                            return
                        elif op[0] == 3:
                            i.codigo = int(x[0]['it_alter'][0][1])
                            return
                        elif op[0] == 4:
                            i.senha = x[0]['it_alter'][0][1]
                            return
                else:
                    self.__tela_adm.mostra_mensagem('Administrador não encontrado',
                                                    'Não foi possível encontrar um administrador com o código passado')

        except IndexError:
            return
        except TypeError:
            return
