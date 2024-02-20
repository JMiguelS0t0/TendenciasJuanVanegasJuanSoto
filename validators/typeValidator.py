import re
from datetime import datetime, timedelta

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
    
    if len(string) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres")

    if not any(char.isupper() for char in string):
        raise ValueError("La contraseña debe contener al menos una mayúscula")

    if not any(char.isdigit() for char in string):
        raise ValueError("La contraseña debe contener al menos un número")

    if not re.search(r"[!@#$%^&*()-_=+{};:,<.>]", string):
        raise ValueError("La contraseña debe contener al menos un carácter especial")
    
    if ' ' in string:
        raise ValueError("La contraseña no debe contener espacios")
    return True

def emailValidator(string, element):
    textValidator(string, element)

    try:
        username, domain = string.split("@")
    except ValueError:
        raise ValueError("El correo electrónico debe contener un arroba (@).")

    if not username or len(username) < 1:
        raise ValueError("El nombre de usuario no puede estar vacío.")

    if not domain or len(domain) < 3:
        raise ValueError("El dominio no puede estar vacío y debe tener al menos 3 caracteres.")

    if not "." in domain:
        raise ValueError("El dominio debe tener al menos un punto.")

    if " " in domain or " " in username:
        raise ValueError("El nombre de usuario y el dominio no deben contener espacios.")

    return True

def phoneNumberValidator(string, element):
    try:
        numberValidator(string, element)
    except ValueError as e:
        raise ValueError("No es un número de teléfono válido") from e

    if not 1 <= len(str(string)) <= 10:
        raise ValueError("El número de teléfono debe tener entre 1 y 10 dígitos.")

    return True

def dateBirthValidator(string, element):
    textValidator(string, element)
    
    try:
        dateBirth = datetime.strptime(string, "%d/%m/%Y")
    except ValueError:
        raise ValueError("No tiene formato de fecha valido (DD/MM/YYYY)")
    
    if dateBirth > datetime.today():
        raise ValueError("No puede ser una fecha en el futuro.")
    
    maxAge = datetime.today() - timedelta(days=365.25 * 150)
    if dateBirth < maxAge:
        raise ValueError("No puede ser mayor a 150 años")
    
    return True

def addressValidator(string, element):
    textValidator(string, element)
    
    if len(string) > 30:
        raise ValueError("No puede tener mas de 30 caracteres.")
    
    return True

def userNameValidator(string, element):
    textValidator(string, element)

    if len(string) > 15:
        raise ValueError("No puede tener más de 15 caracteres.")

    if not re.match("[a-zA-Z0-9]+", string):
        raise ValueError("Solo puede contener letras y números.")

    return True