from View.abtract_tela import AbstractTela


class TelaAdministrador(AbstractTela):
    def opcoes_administrador(self):
        print('-' * 10, 'Administrador', '-' * 10)
        self.tela_opcoes()

    def novo_adm(self):
        print('-' * 10, 'Novo administrador', '-' * 10)
        nome = input('Nome: ')
        senha = input('Senha: ')
        while True:
            try:
                codigo = int(input('Código: '))
                return {'nome': nome, 'senha': senha, 'codigo': codigo}
            except ValueError:
                print('Valor inválido!')

    def mostra_adm(self, nome: str, codigo: int):
        print(10 * '-')
        print(nome)
        print(codigo)
