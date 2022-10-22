from Model.maquina import Maquina


class ControladorMaquina:
    def __init__(self):
        self.__administradores = {}
        self.__produtos = {}
        self.__historico = {}

    @property
    def administradores(self):
        return self.__administradores

    @property
    def produtos(self):
        return self.__produtos

    @property
    def historico(self):
        return self.__historico
