import PySimpleGUI as sg


class TelaAdm:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_mensagem(self, titulo, msg):
        sg.popup(titulo, msg)

    def opcoes_adm(self):
        sg.ChangeLookAndFeel = 'DarkGrey14'
        layout = [

            [sg.Text('Administradores', font=('Times New Roman', 18), size=(30, 1))],
            [sg.Text('Escolha uma opção', font=('Times New Roman', 15))],
            [sg.Text()],
            [sg.Button('Novo administrador', key=1, font=('Times New Roman', 15)),
             sg.Button('Excluir administrador', key=2, font=('Times New Roman', 15)),
             sg.Button('Alterar administrador', key=3, font=('Times New Roman', 15))],
            [sg.Text()],
            [sg.Button('Voltar', key=0, font=('Times New Roman', 12))]

                 ]
        self.__window = sg.Window(title='Administradores').Layout(layout)
        op = (self.open())
        self.close()
        return op[0]

    def dados_adm(self):
        layout = [

            [sg.Text('Insira o nome', size=(30, 1)), sg.InputText(key='it_nome')],
            [sg.Text('Insira o código', size=(30, 1)), sg.InputText(key='it_codigo')],
            [sg.Text('Insira a senha', size=(30, 1)), sg.InputText(password_char='*', key='it_senha')],
            [sg.Text('Confirme sua senha', size=(30, 1)), sg.InputText(password_char='*', key='it_sec_senha')],
            [sg.Button('Cancelar', key=0, font=('Times New Roman', 15)), sg.Button('Confirmar', key=1,
                                                                                   font=('Times New Roman', 15))]

                 ]
        self.__window = sg.Window('Dados Administrador').Layout(layout)
        op = (self.open())
        codigo = (op[1]['it_codigo'])
        senha = (op[1]['it_senha'])
        sec_senha = op[1]['it_sec_senha']
        self.close()
        if senha != sec_senha:
            self.mostra_mensagem('Senha incorreta!', 'Senhas não coincidem.')
            return None
        if op[0] == 0:
            return None
        while True:
            try:
                cod = int(codigo)
                op[1]['it_codigo'] = cod
                return op
            except ValueError:
                self.mostra_mensagem('Código inválido!', 'Somente números inteiros são aceitos')
                return None
            except TypeError:
                return None

    def excluir_adm(self, lista):
        lista_concatenada = []
        for i in lista:
            lista_concatenada.append((i.nome, i.codigo))
        layout = [

            [sg.Text('Escolha o administrador a ser excluído', size=(35, 1),
                     font='Lucida', justification='left')],
            [sg.Listbox(values=lista_concatenada, select_mode='single', key='lb_adm_exc',
                        size=(100, 8))],
            [sg.Button('Voltar', font=('Times New Roman', 15), key=0),
             sg.Button('Confirmar', font=('Times New Roman', 15), key=1)]

                  ]
        self.__window = sg.Window('Excluir Administrador').Layout(layout)
        op = (self.open())
        self.close()
        if op is None:
            return
        return op

    def alterar_administrador(self, lista):
        lista_concatenada = []
        for i in lista:
            lista_concatenada.append((i.nome, i.codigo))
        layout = [

            [sg.Text('Escolha o administrador a ser alterado', size=(35, 1),
                     font='Lucida', justification='left')],
            [sg.Listbox(values=lista_concatenada, select_mode='single', key='lb_adm_alt',
                        size=(100, 8))],
            [sg.Button('Voltar', font=('Times New Roman', 15), key=0),
             sg.Button('Confirmar', font=('Times New Roman', 15), key=1)]

                  ]
        self.__window = sg.Window('Excluir Administrador').Layout(layout)
        op = (self.open())
        self.close()
        if op is None:
            return
        return op

    def opcoes_alteracao(self):
        layout = [

            [sg.Text('O que deseja alterar?', font=('Times New Roman', 15))],
            [sg.Text()],
            [[sg.Button('Nome', key=2, font=('Times New Roman', 15)),
             sg.Button('Código', key=3, font=('Times New Roman', 15)),
             sg.Button('Senha', key=4, font=('Times New Roman', 15))]],
            [sg.Button('Voltar', font=('Times New Roman', 15), key=0),
             sg.Button('Confirmar', font=('Times New Roman', 15), key=1)]

                ]
        self.__window = sg.Window('Alteração').Layout(layout)
        op = (self.open())
        self.close()
        if op is None:
            return
        return op

    def alteracao(self):
        layout = [

            [sg.Text('Novo dado', size=(35, 1), font='Lucida', justification='left')],
            [sg.InputText(key='it_alter')],
            [sg.Button('Voltar', font=('Times New Roman', 15), key=0),
             sg.Button('Confirmar', font=('Times New Roman', 15), key=1)]

                 ]
        self.__window = sg.Window('Alteração').Layout(layout)
        op = (self.open())
        if op is None:
            return
        self.close()
        return op
