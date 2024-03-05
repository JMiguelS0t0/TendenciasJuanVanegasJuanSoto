import re
from datetime import datetime, timedelta

def textValidator(string, element):
    while True:
        try:
            if string is None or string == "":
                raise ValueError(element + " no es un valor válido")
            return string
        except ValueError as e:
            string = input("Formato incorrecto. Ingrese nuevamente el valor para " + element + ": " + str(e) + "\n")

def numberValidator(string, element):
    while True:
        try:
            textValidator(string, element)
            return int(string)
        except ValueError as e:
            string = input("Formato incorrecto. Ingrese nuevamente el valor numérico para " + element + ": " + str(e) + "\n")

def passwordValidator(string, element):
    while True:
        try:
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
            
            return string
        except ValueError as e:
            string = input("Ingrese nuevamente la contraseña para " + element + ": " + str(e) + "\n")

def emailValidator(string, element):
    while True:
        try:
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

            return string
        except ValueError as e:
            string = input("Ingrese nuevamente el correo electrónico para " + element + ": " + str(e) + "\n")

def phoneNumberValidator(string, element):
    while True:
        try:
            string = str(string)
            try:
                numberValidator(string, element)
            except ValueError as e:
                raise ValueError("No es un número de teléfono válido") from e

            if not 1 <= len(string) <= 10:
                raise ValueError("El número de teléfono debe tener entre 1 y 10 dígitos.")

            return string
        except ValueError as e:
            string = input("Ingrese nuevamente el número de teléfono para " + element + ": " + str(e) + "\n")

def validateDateFormat(string, element):
    while True:
        try:
            dateFormat = datetime.strptime(string, "%d/%m/%Y")
            return dateFormat
        except ValueError:
            string = input("Ingrese nuevamente la fecha con formato DD/MM/YYYY para " + element + ": ")

def dateBirthValidator(string, element):
    while True:
        try:
            string = textValidator(string, element)
            dateBirth = validateDateFormat(string, element)

            if dateBirth > datetime.today():
                raise ValueError("La fecha de nacimiento no puede estar en el futuro.")

            maxAge = datetime.today() - timedelta(days=365 * 150)
            if dateBirth < maxAge:
                raise ValueError("La fecha de nacimiento no puede ser mayor a 150 años.")

            return string
        except ValueError as e:
            string = input("Ingrese nuevamente la fecha de nacimiento para " + element + ": " + str(e) + "\n")

def futureDateValidator(string, element):
    while True:
        try:
            date = validateDateFormat(string, element)
            if date < datetime.today():
                raise ValueError("La fecha no puede ser anterior a la fecha actual.")
            return string
        except ValueError:
            string = input("Ingrese nuevamente la fecha para " + element + ": ")

def addressValidator(string, element):
    while True:
        try:
            textValidator(string, element)
            
            if len(string) > 30:
                raise ValueError("No puede tener más de 30 caracteres.")
            
            return string
        except ValueError as e:
            string = input("Ingrese nuevamente la dirección para " + element + ": " + str(e) + "\n")

def userNameValidator(string, element):
    while True:
        try:
            textValidator(string, element)

            if len(string) > 15:
                raise ValueError("No puede tener más de 15 caracteres.")

            if not re.match(r"^[a-zA-Z0-9]+$", string): 
                raise ValueError("Solo puede contener letras y números.")

            return string
        except ValueError as e:
            string = input("Ingrese nuevamente el nombre de usuario para " + element + ": " + str(e) + "\n")
