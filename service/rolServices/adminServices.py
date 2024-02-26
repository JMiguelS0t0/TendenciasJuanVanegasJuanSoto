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

def getAllUsers(hospital):
    return hospital.persons.copy()

def createUser(hospital, name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password):
    user = validateId(hospital, cedula)
    if user:
        raise Exception("Ya existe una persona con esa cedula registrada")
    user = validateUserName(hospital, userName)
    if user: 
        raise Exception("Ya existe un usuario con ese username")
    user = models.Person(name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password)
    hospital.persons.append(user)
    
def updateUser(hospital, cedula, new_name, new_email, new_phoneNumber, new_dateBirth, new_address, new_userName, new_password):
    for person in hospital.persons:
         if person.cedula == cedula:
            person.name = new_name
            person.email = new_email
            person.phoneNumber = new_phoneNumber
            person.dateBirth = new_dateBirth
            person.address = new_address
            person.userName = new_userName
            person.password = new_password
            print("Usuario actualizado exitosamente.")
            return
    print("No se encontró ningún usuario con esa identificación.")

def deleteUser(hospital, cedula):
    for person in hospital.persons:
        if person.cedula == cedula:
            return True
    return False