class TelaBebida:

    def opcoes_administrador(self):
        print('-------------', 'Bebidas', '---------------')
        self.tela_opcoes()
        op = self.le_num_inteiro('Opção: ', [0, 1, 2, 3, 4])
        return op

    def nova_bebida(self):
        print('-------------', 'Nova bebida', '---------------')
        nome = input('Coloque o nome da comida: ')
        codigo = input('Coloque o codigo da comida: ')
        preco = input('Coloque o preço da comida: ')
        quantidade = input('Coloque a quantidade da comida: ')
        tipo = input('Coloque o tipo: ')

    def mostra_comida(self, nome: str, codigo: int, preco: float, quantidade: int, tipo: str):
        print(print('-------------', 'bebida', '---------------'))
        print('Nome: ', nome)
        print('Código: ', codigo)
        print('Preco: ', preco)
        print('Quantidade: ', quantidade)
        print('Tipo: ', tipo)
