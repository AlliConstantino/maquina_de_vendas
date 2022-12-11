from View.abtract_tela import AbstractTela


class TelaProduto(AbstractTela):
    def opcoes_produto(self):
        print('-------------', 'Produtos', '---------------')
        self.tela_opcoes()
        op = self.le_num_inteiro('Opção: ', [0, 1, 2, 3, 4])
        return op

    def novo_produto(self):
        print('-------------', 'Novo Produto', '---------------')
        nome = input('Coloque o nome do produto: ')
        while True:
            try:
                codigo = int(input('Código: '))
                break
            except ValueError:
                print('Valor inválido!')
        while True:
            try:
                preco = float(input('Preço: '))
                break
            except ValueError:
                print('Valor inválido!')
        while True:
            try:
                quantidade = int(input('Quantidade: '))
                break
            except ValueError:
                print('Valor inválido!')

        while True:
            #
            tipo = input('Tipo: ')
            break

            return {'nome': nome, 'codigo': codigo, 'preco': preco, 'quantidade': quantidade, 'tipo': tipo}

    def mostra_produto(self, nome: str, codigo: int, preco: float, quantidade: int, tipo: str):
        print(print('-------------', 'Produtos', '---------------'))
        print('Nome: ', nome)
        print('Código: ', codigo)
        print('Preco: ', preco)
        print('Quantidade: ', quantidade)
        print('Tipo: ', tipo)

    def pega_dados(self):
        nome = input('Nome: ')
        while True:
            try:
                codigo = int(input('Código: '))
                break
            except ValueError:
                print('Valor inválido!')
        while True:
            try:
                preco = float(input('Preço: '))
                break
            except ValueError:
                print('Valor inválido!')
        while True:
            try:
                quantidade = int(input('Quantidade: '))
                break
            except ValueError:
                print('Valor inválido!')

        while True:
                tipo = input('Tipo: ')
                break
        return {'nome': nome, 'codigo': codigo, 'preco': preco,  'quantidade': quantidade, 'tipo': tipo}
