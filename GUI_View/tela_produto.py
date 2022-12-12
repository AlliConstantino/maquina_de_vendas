#import PySimpleGUI as sg


class TelaProduto:
    def __init__(self):
        self.__window = None

    def close(self):
        self.__window.Close()

    def open(self):
        button, values = self.__window.Read()
        return button, values

    def mostra_mensagem(self, titulo, msg):
        sg.popup(titulo, msg)

    def opcoes_produto(oself):
        sg.ChangeLookAndFeel = 'DarkGrey14'
        layout = [

            [sg.Text('PRODUTOS', font=('Times New Roman', 18), size=(30, 1))],
            [sg.Text()],
            [sg.Button('Novo produto', key=1, font=('Times New Roman', 15)),
             sg.Button('Excluir produto', key=2, font=('Times New Roman', 15)),
             sg.Button('Alterar produto', key=3, font=('Times New Roman', 15))],
            [sg.Text()],
            [sg.Button('Voltar', key=0, font=('Times New Roman', 12))]

                 ]
        self.__window = sg.Window(title='PRODUTOS').Layout(layout)
        op = (self.open())
        self.close()
        return op[0]

    def dados_produto(self):
        layout = [

            [sg.Text('Insira o nome: ', size=(30, 1)), sg.InputText(key='it_nome')],
            [sg.Text('Insira o codigo: ', size=(30, 1)), sg.InputText(key='it_codigo')],
            [sg.Text('Insira o preco: ', size=(30, 1)), sg.InputText(key='it_preco')],
            [sg.Text('Insira o quantidade: ', size=(30, 1)), sg.InputText(key='it_quantidade')],
            [sg.Text('Insira o tipo: ', size=(30, 1)), sg.InputText(key='it_tipo')],
            [sg.Button('Cancelar', key=0, font=('Times New Roman', 15)), sg.Button('Confirmar', key=1,
                                                                                   font=('Times New Roman', 15))]

                 ]
        self.__window = sg.Window('Dados Produto').Layout(layout)
        op = (self.open())
        nome = (op[1]['it_nome'])
        codigo = (op[2]['it_senha'])
        temp_codigo = op[3]['it_temp_codigo']
        preco = (op[4]['it_preco'])
        quantidade = (op[5]['it_quantidade'])
        tipo = (op[6]['it_tipo'])
        self.close()
        if codigo != temp_codigo:
            self.mostra_mensagem('Codigo errado, tente outra vez', 'Codigos não estão iguais.')
            return None
        if op[0] == 0:
            return None
        while True:
            try:
                cod = int(codigo)
                op[1]['it_codigo'] = cod
                return op
            except ValueError:
                self.mostra_mensagem('Codigo esta errado!', 'Insira apenas numeros')
                return None
            except TypeError:
                return None

    def excluir_produto(self, lista):
        lista_de_produtos = []
        for i in lista:
            lista_de_produtos.append((i.nome, i.codigo, i.preco, i.quantidade, i.tipo))
        layout = [

            [sg.Text('Selecione o produto: ', size=(35, 1),font='Times New Roman', justification='left')],
            [sg.Listbox(values = lista_de_produtos, select_mode='single', key='lista_produtos', size=(100, 8))],
            [sg.Button('Voltar', font=('Times New Roman', 15), key=0), sg.Button('Confirmar', font=('Times New Roman', 15), key=1)]

                  ]

        self.__window = sg.Window('Excluir produto').Layout(layout)
        op = (self.open())
        self.close()
        if op is None:
            return
        return op

    def alterar_produto(self, lista):
        lista_produto = []
        for i in lista:
            lista_produto.append((i.nome, i.codigo))
        layout = [

            [sg.Text('Qual o produto sera alterado? ', size=(35, 1), font='Times New Roman', justification='left')],
            [sg.Listbox(values = lista_produto, select_mode='single', key='lista_produtos',size=(100, 8))],
            [sg.Button('Voltar', font=('Times New Roman', 15), key=0),
             sg.Button('Confirmar', font=('Times New Roman', 15), key=1)]

                  ]
        self.__window = sg.Window('Atenção: Excluir produto!').Layout(layout)
        op = (self.open())
        self.close()
        if op is None:
            return
        return op

    def opcoes_alteracao(self):
        layout = [

            [sg.Text('O que sera alterado ?', font=('Times New Roman', 15))],
            [sg.Text()],
            [[sg.Button('Nome', key=2, font=('Times New Roman', 15)),
             sg.Button('Código', key=3, font=('Times New Roman', 15)),
             sg.Button('Preco', key=4, font=('Times New Roman', 15))]],
             sg.Button('Quantidade', key=5, font=('Times New Roman', 15)),
             sg.Button('Tipo', key=6, font=('Times New Roman', 15)),
            [sg.Button('Voltar', font=('Times New Roman', 12), key=0)]

                ]
        self.__window = sg.Window('Atencao! Produto sera alterado').Layout(layout)
        op = (self.open())
        self.close()
        if op is None:
            return
        return op

    def alteracao(self):
        layout = [

            [sg.Text('Novo produto', size=(35, 1), font='Times New Roman', justification='left')],
            [sg.InputText(key='it_produto_alterado')],
            [sg.Button('Cancelar', font=('Times New Roman', 12), key=0),
             sg.Button('Confirmar', font=('Times New Roman', 12), key=1)]

                 ]
        self.__window = sg.Window('Alteracao').Layout(layout)
        op = (self.open())
        self.close()
        if op is None:
            return
        if len(op[1]['it_produto_alterado']) == 0:
            return None
        return op
