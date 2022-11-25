class AdmDuplicadoException(Exception):
    def __init__(self):
        super().__init__('Administrador já existe!')
