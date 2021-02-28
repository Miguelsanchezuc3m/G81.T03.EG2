"""Modulo X"""


class AccessManagementException(Exception):
    """Aqui se encontraria el comentario del funcionamiento de la clase."""
    def __init__(self, message):
        self.__message = message
        super().__init__(self.message)

    @property
    def message(self):
        """Comentario"""
        return self.__message

    @message.setter
    def message(self, value):
        self.__message = value
