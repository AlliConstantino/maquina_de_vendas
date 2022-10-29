from abc import ABC


class AbstractTela(ABC):
    def le_num_inteiro(self, mensagem: str = '', inteiros_validos: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print('Valor incorreto: Digite um valor numerico inteiro válido')
                if inteiros_validos:
                    print('Valores válidos: ', inteiros_validos)

    def tela_opcoes(self):
        print("Escolha a opção")
        print("1 - Novo")
        print("2 - Excluir")
        print('3 - Listar')
        print('4 - Alterar')
        print("0 - Retornar")

    def mostra_msg(self, msg):
        print(msg)

    def pega_codigo(self):
        while True:
            try:
                cod = int(input('Insira o código: '))
                return cod
            except ValueError:
                print('Valor inválido!')
