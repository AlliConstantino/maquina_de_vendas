import PySimpleGUI as sg


class TelaGerencia:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_mensagem(self, titulo, msg):
        sg.popup(titulo, msg)

    def opcoes_gerencia(self):
        layout = [

            [sg.Text('Gerência', font=('Times New Roman', 18))],
            [sg.Text('Escolha uma opção', font=('Times New Roman', 15))],
            [sg.Text()],
            [sg.Button('Produtos', key=1, font=('Times New Roman', 15)),
             sg.Button('Administradores', key=2, font=('Times New Roman', 15))],
            [sg.Text()],
            [sg.Button('Voltar', key=0, font=('Times New Roman', 12))]

                 ]
        self.__window = sg.Window(title='Gerência').Layout(layout)
        op = (self.open())
        self.close()
        return op[0]

    def logar(self):
        layout = [

            [sg.Text('Código', size=(5, 1)), sg.InputText(key='it_codigo')],
            [sg.Text('Senha', size=(5, 1)), sg.InputText(password_char='*', key='it_senha')],
            [sg.Button('Voltar', font=('Times New Roman', 12), key=0),
             sg.Button('Confirmar', font=('Times New Roman', 12), key=1)]

                 ]
        self.__window = sg.Window(title='Gerência').Layout(layout)
        op = (self.open())
        self.close()
        codigo = (op[1]['it_codigo'])
        if op[0] == 0:
            return None
        while True:
            try:
                cod = int(codigo)
                op[1]['it_codigo'] = cod
                return cod, (op[1]['it_senha'])
            except ValueError:
                self.mostra_mensagem('Código inválido!', 'Somente números inteiros são aceitos')
                return None
            except TypeError:
                return None
