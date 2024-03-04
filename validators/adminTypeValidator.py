from .typeValidator import *
from service.rolServices import adminServices

def createUser(hospital, rol):
    cedula = numberValidator(input("Ingrese la cedula de: " +  rol + "\n"), "Cedula de " + rol)
    name = textValidator(input("Ingrese el nombre del: " + rol + "\n"), "Nombre de: " +  rol)
    email = emailValidator(input("Ingrese el correo del: " + rol + "\n"), "Email de: " + rol)
    phoneNumber = phoneNumberValidator(input("Ingrese el numero de telefono de: " +  rol + "\n"), "Numero de " + rol)
    dateBirth = dateBirthValidator(input("Ingrese la fecha de nacimiento del: " + rol + "(DD/MM/YYYY)\n"), "Fecha de: " +  rol)
    address = addressValidator(input("Ingrese la direccion del: " + rol + "\n"), "La direccion de: " + rol)
    userName = userNameValidator(input("Ingrese usuario del: " + rol + "\n"), "El nombre de usuario de: " + rol)
    password = passwordValidator(input("Ingrese la contraseña:\n"), "Contraseña de: " + rol)
    adminServices.createUser(hospital, name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password)

def updateUser(hospital, cedula):
    newName = textValidator(input("Ingrese el nuevo nombre del usuario:\n"), "Nuevo nombre de usuario")
    newEmail = emailValidator(input("Ingrese el nuevo correo del usuario:\n"), "Nuevo correo del usuario")
    newPhoneNumber = phoneNumberValidator(input("Ingrese el nuevo número de teléfono del usuario:\n"), "Nuevo número de teléfono del usuario")
    newDateBirth = dateBirthValidator(input("Ingrese la nueva fecha de nacimiento del usuario (DD/MM/YYYY):\n"), "Nueva fecha de nacimiento del usuario")
    newAddress = addressValidator(input("Ingrese la nueva dirección del usuario:\n"), "Nueva dirección del usuario")
    newUserName = userNameValidator(input("Ingrese el nuevo nombre de usuario del usuario:\n"), "Nuevo nombre de usuario del usuario")
    newPassword = passwordValidator(input("Ingrese la nueva contraseña del usuario:\n"), "Nueva contraseña del usuario")
    adminServices.updateUser(hospital, cedula, newName, newEmail, newPhoneNumber, newDateBirth, newAddress, newUserName, newPassword)

def getAllUsers(hospital):
    allUsers = adminServices.getAllUsers(hospital)  
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

def deleteUserById(hospital, cedula):
    cedula = int(cedula)
    if adminServices.deleteUser(hospital, cedula):
        deleteUser(hospital, cedula)
    else:
        print("No se encontró ningun usuario con esa identificación")

def deleteUser(hospital, cedula):
    for i, person in enumerate(hospital.persons):
        if person.cedula == cedula:
            del hospital.persons[i]
            print("Usuario eliminado exitosamente.")
            return 
