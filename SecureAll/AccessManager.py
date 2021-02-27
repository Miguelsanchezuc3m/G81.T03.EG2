import json
from .AccessManagementException import AccessManagementException
from .AccessRequest import AccessRequest

class AccessManager:
    def __init__(self):
        pass


    def ValidateDNI(self, DNI):

        letra = DNI[-1]
        numero = DNI[:-1]

        if numero.isnumeric() == False:
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




    def ReadaccessrequestfromJSON(self, fi):

        try:
            with open(fi) as f:
                DATA = json.load(f)
        except FileNotFoundError as e:
            raise AccessManagementException("Wrong file or file path") from e
        except json.JSONDecodeError as e:
            raise AccessManagementException("JSON Decode Error - Wrong JSON Format") from e


        try:
            idDoc = DATA["id"]
            name = DATA["name"]
            req = AccessRequest(idDoc, name)
        except KeyError as e:
            raise AccessManagementException("JSON Decode Error - Invalid JSON Key") from e
        if not self.ValidateDNI(idDoc):
            raise AccessManagementException("Invalid DNI")

        # Close the file
        return req