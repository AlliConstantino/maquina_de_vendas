import PySimpleGUI as sg


class TelaAdm:
    def __init__(self):
        self.__window = None
        self.opcoes_adm()

    def opcoes_adm(self):
        sg.ChangeLookAndFeel = 'DarkGrey14'
        layout = [

            [sg.Text('Administradores', font=('Helvetica', 18))],
            [sg.Text('Escolha uma opção', font=('Helvetica', 12))],
            [sg.Text()],
            [sg.Button('Novo administrador', key=1),
             sg.Button('Excluir administrador', key=2),
             sg.Button('Alterar administrador', key=3)],
            [sg.Text()],
            [sg.Button('Voltar', key=0)]

                 ]
        self.__window = sg.Window(title='Administradores').Layout(layout)
        op = (self.open())
        self.close()
        return op[0]

    def dados_adm(self):
        sg.ChangeLookAndFeel = 'DarkGrey14'
        layout = [

            [sg.Text('Nome:'), sg.InputText(key='it_nome')],
            [sg.Text('Código'), sg.InputText(key='it_codigo')],
            [sg.Button('Cancelar', key=0), sg.Button('Confirmar', key=1)]

                 ]
        self.__window = sg.Window('Dados Administrador').Layout(layout)
        button, values = self.__window.Read()
        print(button, values)

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_mensagem(self, msg):
        sg.popup(msg)
