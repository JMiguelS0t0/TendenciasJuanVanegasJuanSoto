import model.models as models

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

def getAllUsers(hospital):
    return hospital.persons.copy()

def getPersonById(hospital, cedula):
    for person in hospital.persons:
        if str(person.cedula) == str(cedula):
            return person
    return None

def createUser(hospital, name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password):
    user = models.Person(name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password)
    hospital.persons.append(user)
    
def updateUser(hospital, cedula, newName=None, newEmail=None, newPhoneNumber=None, newDateBirth=None, newAddress=None, newUserName=None, newPassword=None):
    person = getPersonById(hospital, cedula)
    if person:
        if newName != "No update":
            person.name = newName
        if newEmail != "No update" and newEmail != None:
            person.email = newEmail
        if newPhoneNumber != "No update" and newPhoneNumber != None:
            person.phoneNumber = newPhoneNumber
        if newDateBirth != "No update" and newDateBirth != None:
            person.dateBirth = newDateBirth
        if newAddress != "No update":
            person.address = newAddress
        if newUserName != "No update":
            person.userName = newUserName
        if newPassword != "No update" and newPassword != None:
            person.password = newPassword
        print("Usuario actualizado exitosamente.")
        return
    raise Exception("No se encontró un usuario con esa cedula")

def deleteUserById(hospital, cedula):
    person = getPersonById(hospital, cedula)
    if person:
        hospital.persons.remove(person)
        print("Usuario eliminado exitosamente.")
        return True
    raise Exception("No se encontró un usuario con esa cedula")
