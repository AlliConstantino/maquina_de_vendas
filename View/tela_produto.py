from View.abtract_tela import AbstractTela


class TelaProduto(AbstractTela):

    #deixar, mas revisar depois
    def opcoes_produto(self):
        print('-------------', 'Produtos', '---------------')
        self.tela_opcoes()
        op = self.le_num_inteiro('Opção: ', [0, 1, 2, 3, 4])
        return op

    def novo_produto(self):
        print('-------------', 'Novo Produto', '---------------')
        nome = input('Coloque o nome do produto: ')
        codigo = input('Coloque o codigo do produto: ')
        preco = input('Coloque o preço do produto: ')
        quantidade = input('Coloque a quantidade do produto: ')
        tipo = input('Coloque o tipo do produto: ')
        return {'nome': nome, 'codigo': codigo, 'preco': preco, 'quantidade': quantidade, 'tipo': tipo}

    def mostra_produto(self, nome: str, codigo: int, preco: float, quantidade: int):
        print(print('-------------', 'Produtos', '---------------'))
        print('Nome: ', nome)
        print('Código: ', codigo)
        print('Preco: ', preco)
        print('Quantidade: ', quantidade)
