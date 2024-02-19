import re

def textValidator(string,element):
    if string==None or string=="":
        raise Exception(element + "no es un valor es valido")

def numberValidator(string,element):
    textValidator(string,element)
    try:
        return int(string)
    except:
        raise Exception(element + " no es un numero valido")
    
def passwordValidator(string, element):
    textValidator(string, element)
    
    if len(string) < 8 or not any(char.isdigit() for char in string) or not re.search(r"[!@#$%^&*()-_=+{};:,<.>]", string) or ' ' in string:
        raise Exception("La contraseña debe tener al menos 8 caracteres, contener al menos un número, al menos un carácter especial y no contener espacios.")
