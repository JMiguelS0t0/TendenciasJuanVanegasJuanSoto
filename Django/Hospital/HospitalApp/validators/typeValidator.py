import re
from datetime import datetime, timedelta

def textValidator(string, element):
    if not string or string.strip() == "":
        raise ValueError(element + " no puede estar vacío.")
    return string

def textValidatorNone(string, element):
    if not string or string.strip() == "":
        return None
    return string.strip()


def booleanValidator(string, element):
    if not isinstance(string, str):
        raise ValueError(element + " debe ser una cadena.")
    if string.lower() not in ['true', 'false']:
        raise ValueError(element + " debe ser un valor booleano.")
    return string.lower() == 'true'

def numberValidator(value, element):
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        raise ValueError(element + " debe ser un valor numérico.")


def passwordValidator(string, element):
    if len(string) < 8:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")

    if not re.search(r"(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()-_=+{};:,<.>])", string):
        raise ValueError("La contraseña no cumple con los requisitos de seguridad.")

    if ' ' in string:
        raise ValueError("La contraseña no debe contener espacios.")
    
    return string

def emailValidator(string, element):
    if not re.match(r"[^@]+@[^@]+\.[^@]+", string):
        raise ValueError("El correo electrónico no es válido.")
    return string

def phoneNumberValidator(string, element):
    string = str(string)
    if not 1 <= len(string) <= 10 or not string.isdigit():
        raise ValueError("El número de teléfono debe tener entre 1 y 10 dígitos.")
    return string

def validateDateFormat(string, element):
    try:
        return datetime.strptime(string, "%d/%m/%Y")
    except ValueError:
        raise ValueError("Formato de fecha incorrecto para " + element + ". Debe ser en formato DD/MM/YYYY.")

def dateBirthValidator(string, element):
    dateBirth = validateDateFormat(string, element)

    if dateBirth > datetime.today():
        raise ValueError("La fecha de nacimiento no puede estar en el futuro.")

    maxAge = datetime.today() - timedelta(days=365 * 150)
    if dateBirth < maxAge:
        raise ValueError("La fecha de nacimiento no puede ser mayor a 150 años.")

    return dateBirth

def futureDateValidator(string, element):
    date = validateDateFormat(string, element)
    if date < datetime.today():
        raise ValueError("La fecha no puede ser anterior a la fecha actual.")
    return date

def addressValidator(string, element):
    if len(string) > 30:
        raise ValueError("La dirección no puede tener más de 30 caracteres.")
    return string

def userNameValidator(string, element):
    if len(string) > 15:
        raise ValueError("El nombre de usuario no puede tener más de 15 caracteres.")

    if not re.match(r"^[a-zA-Z0-9]+$", string): 
        raise ValueError("El nombre de usuario solo puede contener letras y números.")

    return string