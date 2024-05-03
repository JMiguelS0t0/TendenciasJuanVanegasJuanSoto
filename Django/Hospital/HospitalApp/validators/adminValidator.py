from .typeValidator import *
from HospitalApp.service.rolService import adminService

# --------- POST
def createUser(name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password):
    cedula = numberValidator(cedula, "Cedula de " + rol)
    rol = textValidator(rol, "Rol de: " + rol)
    name = textValidator(name, "Nombre de: " +  rol)
    email = emailValidator(email, "Email de: " + rol)
    phoneNumber = phoneNumberValidator(phoneNumber, "Numero de " + rol)
    dateBirth = dateBirthValidator(dateBirth, "Fecha de: " +  rol)
    address = addressValidator(address, "La direccion de: " + rol)
    userName = userNameValidator(userName, "El nombre de usuario de: " + rol)
    password = passwordValidator(password, "Contraseña de: " + rol)
    adminService.createUser(name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password)

# --------- GET
def getUser(cedula):
    cedula = numberValidator(cedula, "Cedula de usuario")
    return adminService.getUser(cedula)

def getUsers():
    return adminService.getUsers()

# --------- DELETE
def deleteUser(cedula):
    return adminService.deleteUser(cedula)


# --------- UPDATE
def updateUser(name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password):
    cedula = numberValidator(cedula, "Cedula de usuario")
    rol = textValidator(rol, "Rol de usuario")
    name = textValidator(name, "Nombre de usuario")
    email = emailValidator(email, "Email de usuario")
    phoneNumber = phoneNumberValidator(phoneNumber, "Numero de usuario")
    dateBirth = dateBirthValidator(dateBirth, "Fecha de usuario")
    address = addressValidator(address, "La direccion de usuario")
    userName = userNameValidator(userName, "El nombre de usuario de usuario")
    password = passwordValidator(password, "Contraseña de usuario")
    return adminService.updateUser(name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password)
