import PySimpleGUI as sg


class TelaMaquina:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_mensagem(self, titulo, msg):
        sg.popup(titulo, msg)

    def opcoes_maquina(self):
        sg.ChangeLookAndFeel = 'DarkGrey14'
        layout = [

            [sg.Text('Máquina de vendas', font=('Times New Roman', 18))],
            [sg.Text('Escolha uma opção', font=('Times New Roman', 15))],
            [sg.Text()],
            [sg.Button('Vendas', key=1, font=('Times New Roman', 15)),
             sg.Button('Gerência', key=2, font=('Times New Roman', 15))],
            [sg.Text()],
            [sg.Button('Sair', key=0, font=('Times New Roman', 12))]

                 ]
        self.__window = sg.Window(title='Administradores').Layout(layout)
        op = (self.open())
        self.close()
        print(op)
        return op[0]
