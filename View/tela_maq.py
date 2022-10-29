from View.abtract_tela import AbstractTela


class TelaMaquina(AbstractTela):
    def opcoes_maq(self):
        print('1 - Vendas')
        print('2 - Gerência')
        print('0 - Sair')
        op = self.le_num_inteiro('Opção: ', [1, 2, 0])
        return op
