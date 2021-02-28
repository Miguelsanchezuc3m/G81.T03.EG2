"""Modulo X"""


import json
from datetime import datetime

class AccessRequest:
    """Aqui se encontraria el comentario del funcionamiento de la clase."""
    def __init__(self, id_document, full_name):
        self.__name = full_name
        self.__id_document = id_document
        justnow = datetime.utcnow()
        self.__time_stamp = datetime.timestamp(justnow)

    def __str__(self):
        return "AccessRequest:" + json.dumps(self.__dict__)

    @property
    def name(self):
        """Comentario"""
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def id_document(self):
        """Comentario"""
        return self.__id_document
    @id_document.setter
    def id_document(self, value):
        self.__id_document = value
