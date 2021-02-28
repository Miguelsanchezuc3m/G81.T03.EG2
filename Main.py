"""Modulo X"""


from SecureAll import AccessManager

def main():
    """Comentario"""
    mng = AccessManager()
    res = mng.ReadaccessrequestfromJSON("test.json")
    print(res)







if __name__ == "__main__":
    main()
