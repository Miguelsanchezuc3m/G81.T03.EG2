"""Modulo X"""


import json
from .AccessManagementException import AccessManagementException
from .AccessRequest import AccessRequest

class AccessManager:
    """Aqui se encontraria el comentario del funcionamiento de la clase."""
    def __init__(self):
        pass


    def ValidateDNI(self, dni):
        """Este método comprueba que el formato del DNI es válido y la letra se corresponde con la
        regulación vigente"""

        letra = dni[-1]
        numero = dni[:-1]

        if not numero.isnumeric():
            return False

        if len(numero) > 8 or len(numero) < 7:
            return False

        if len(numero) == 8:
            lista = ["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V"
                 ,"H","L","C","K","E"]
            resto = int(numero) % 23
            if letra != lista[resto]:
                return False

        if len(numero) == 7:
            lista = ["X","Y","Z"]
            resto = int(numero) % 3
            if letra != lista[resto]:
                return False

        return True

    def ReadaccessrequestfromJSON(self, variable_fi):
        """Comentario"""

        try:
            with open(variable_fi) as variable_f:
                data = json.load(variable_f)
        except FileNotFoundError as variable_e:
            raise AccessManagementException("Wrong file or file path") from variable_e
        except json.JSONDecodeError as variable_e:
            raise AccessManagementException("JSON Decode Error - Wrong JSON Format") from variable_e


        try:
            id_doc = data["id"]
            name = data["name"]
            req = AccessRequest(id_doc, name)
        except KeyError as variable_e:
            raise AccessManagementException("JSON Decode Error - Invalid JSON Key") from variable_e
        if not self.ValidateDNI(id_doc):
            raise AccessManagementException("Invalid DNI")

        # Close the file
        return req
