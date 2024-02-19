from .typeValidator import *
from service.rolServices import adminServices as AS

def createUser(hospital, rol):
    cedula = numberValidator(input("Ingrese la cedula de: " +  rol + "\n"), "Cedula de " + rol)
    name = input("Ingrese el nombre del: " + rol + "\n")
    textValidator(name, "Nombre de: " +  rol)
    email = input("Ingrese el correo del: " + rol + "\n")
    dateBirth = input("Ingrese la fecha de nacimiento del: " + rol + "\n")
    address = input("Ingrese la direccion del: " + rol + "\n")
    userName = input("Ingrese usuario del: " + rol + "\n")
    password = input("Ingrese la contraseña:\n")
    passwordValidator(password, "Contraseña de: " + rol)
    AS.createUser(hospital, name, cedula, email, dateBirth, address, rol, userName, password)
