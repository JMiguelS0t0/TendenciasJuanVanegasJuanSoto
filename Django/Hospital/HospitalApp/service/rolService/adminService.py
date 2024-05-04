from HospitalApp import models

def validateId(hospital, cedula):
    for person in hospital.persons:
        if person.cedula == cedula:
            return True
    return False

def validateUserName(hospital, userName):
    for person in hospital.persons:
        if person.userName == userName:
            return True
    return False

# -------------- POST
def createUser(name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password):
    user = models.Person.objects.filter(cedula = cedula)
    if user.exists():
        raise Exception("Ya existe un usuario con esa cedula")
    user = None
    if userName != "N/A":
        user = models.Person.objects.filter(userName = userName)
        if user.exists():
            raise Exception("Ya existe un usuario con ese nombre de usuario")
    user = models.Person(name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password)
    user.save()
    
# -------------- GET
def getUsers():
    try:
        users = models.Person.objects.all()
        if users:
            return users
        else:
            raise Exception("No hay usuarios registrados")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener los usuarios: " + str(e))

def getUser(cedula):
    try:
        user = models.Person.objects.filter(cedula = cedula).first()
        if user:
            return user
        else:
            raise Exception("El usuario no existe, ingrese una cedula valida")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener el usuario: " + str(e))

# -------------- DELETE
def deleteUser(cedula):
    try:
        user = models.Person.objects.filter(cedula = cedula).first()
        if user:
            user.delete()
        else:
            raise Exception("El usuario no existe, ingrese una cedula valida")
    except Exception as e:
        raise Exception("Ocurrio un error al eliminar el usuario: " + str(e))

# -------------- UPDATE
def updateUser(name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password):
    user = models.Person.objects.filter(cedula=cedula).first()
    if user:
        user.name = name
        user.email = email
        user.phoneNumber = phoneNumber
        user.dateBirth = dateBirth
        user.address = address
        user.rol = rol
        user.userName = userName
        user.password = password
        user.save()
    else:
        raise Exception("No se encontró ningún usuario con la cédula proporcionada.")
