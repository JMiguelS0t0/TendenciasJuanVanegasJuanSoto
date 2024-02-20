from .typeValidator import *
from service.rolServices import adminServices as AS

def createUser(hospital, rol):
    cedula = numberValidator(input("Ingrese la cedula de: " +  rol + "\n"), "Cedula de " + rol)
    name = textValidator(input("Ingrese el nombre del: " + rol + "\n"), "Nombre de: " +  rol)
    email = emailValidator(input("Ingrese el correo del: " + rol + "\n"), "Email de: " + rol)
    phoneNumber = phoneNumberValidator(input("Ingrese el numero de telefono de: " +  rol + "\n"), "Numero de " + rol)
    dateBirth = dateBirthValidator(input("Ingrese la fecha de nacimiento del: " + rol + "(DD/MM/YYYY)\n"), "Fecha de: " +  rol)
    address = addressValidator(input("Ingrese la direccion del: " + rol + "\n"), "La direccion de: " + rol)
    userName = userNameValidator(input("Ingrese usuario del: " + rol + "\n"), "El nombre de usuario de: " + rol)
    password = passwordValidator(input("Ingrese la contraseña:\n"), "Contraseña de: " + rol)
    AS.createUser(hospital, name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password)

def getAllUsers(hospital):
    allUsers = AS.getAllUsers(hospital)
    for user in allUsers:
        print(f"Nombre: {user.name}")
        print(f"Cedula: {user.cedula}")
        print(f"Email: {user.email}")
        print(f"Telefono: {user.phoneNumber}")
        print(f"Fecha de nacimiento: {user.dateBirth}")
        print(f"Direccion: {user.address}")
        print(f"Rol: {user.rol}")
        print(f"Usuario: {user.userName}")
        print("-" * 20)

