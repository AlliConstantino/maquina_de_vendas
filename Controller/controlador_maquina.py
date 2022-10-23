from Controller.controlador_administrador import ControladorAdministrador


class ControladorMaquina:
    def __init__(self):
        self.__administradores = []
        self.__produtos = []
        self.__historico = []
        self.__controlador_adm = ControladorAdministrador(self)

    @property
    def administradores(self):
        return self.__administradores

    @property
    def produtos(self):
        return self.__produtos

    @property
    def historico(self):
        return self.__historico
