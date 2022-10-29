from View.abtract_tela import AbstractTela


class TelaGerencia(AbstractTela):
    def opcoes_gerencia(self):
        print(10 * '-', 'Gerência', 10 * '-')
        print('1 - Produtos')
        print('2 - Administradores')
        print('0 - Voltar')
        op = self.le_num_inteiro('Opção: ', [1, 2, 0])
        return op
