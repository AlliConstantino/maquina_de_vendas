from Model.administrador import Administrador
from DAO.dao import DAO


class AdministradorDao(DAO):
    def __init__(self):
        super().__init__('administradores.pkl')

    def add(self, key, obj):
        super().add(key, obj)

    def remove(self, key):
        return super().remove(key)

    def get(self, key):
        return super().get(key)

    def get_all(self):
        return super().get_all()
