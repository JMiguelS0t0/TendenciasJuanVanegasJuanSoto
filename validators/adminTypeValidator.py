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
    newName = input("Ingrese el nuevo nombre del usuario:\n") or "No update"
    newName = textValidator(newName, "Nuevo nombre de usuario")
    
    newEmail = None
    newEmail = input("Ingrese el nuevo correo del usuario:\n") or "No update"
    if newEmail != "No update":
        newEmail = emailValidator(newEmail, "Nuevo correo del usuario")
    
    newPhoneNumber = None
    newPhoneNumber = input("Ingrese el nuevo número de teléfono del usuario:\n") or "No update"
    if newPhoneNumber != "No update":
        newPhoneNumber = phoneNumberValidator(newPhoneNumber, "Nuevo número de teléfono del usuario")
    
    newDateBirth = None
    newDateBirth = input("Ingrese la nueva fecha de nacimiento del usuario (DD/MM/YYYY):\n") or "No update"
    if newDateBirth != "No update":
        newDateBirth = dateBirthValidator(newDateBirth, "Nueva fecha de nacimiento del usuario")
    
    newAddress = input("Ingrese la nueva dirección del usuario:\n") or "No update"
    if newAddress != "No update":
        newAddress = addressValidator(newAddress, "Nueva dirección del usuario")
    
    newUserName = None
    newUserName = input("Ingrese el nuevo nombre de usuario del usuario:\n") or "No update"
    if newUserName != "No update":
        newUserName = userNameValidator(newUserName, "Nuevo nombre de usuario del usuario")
    
    newPassword = None
    newPassword = input("Ingrese la nueva contraseña del usuario:\n") or "No update"
    if newPassword != "No update":
        newPassword = passwordValidator(newPassword, "Nueva contraseña del usuario")

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

def deleteUser(hospital, cedula):
    cedula = input("Ingrese la cedula del usuario a eliminar:\n")
    adminServices.deleteUserById(hospital, cedula)
