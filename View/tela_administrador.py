from View.abtract_tela import AbstractTela


class TelaAdministrador(AbstractTela):
    def opcoes_administrador(self):
        print("-------- Administrador ----------")
        self.tela_opcoes()
