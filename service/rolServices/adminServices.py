import model.models as models

def validateId(hospital, cedula):
    for person in hospital.persons:
        if person.cedula == cedula:
            return person
    return None

def validateUserName(hospital, userName):
    for person in hospital.persons:
        if person.userName == userName:
            return person
    return None

def getAll():
    pass

def createUser(hospital, name, cedula, email, dateBirth, address, rol, userName, password):
    user = validateId(hospital, cedula)
    if user:
        raise Exception("Ya existe una persona con esa cedula registrada")
    user = validateUserName(hospital, userName)
    if user: 
        raise Exception("Ya existe un usuario con ese username")
    user = models.Person(name, cedula, email, dateBirth, address, rol, userName, password)
    hospital.persons.append(user)
    
def eliminateUser():
    pass

