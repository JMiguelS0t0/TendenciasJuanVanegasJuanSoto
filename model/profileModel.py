class Person():
    def __init__(self, id, name, cedula, email, dateBirth, address, rol, userName, password):
        self.id = id
        self.name = name
        self.cedula = cedula
        self.email = email
        self.dateBirth = dateBirth
        self.address = address
        self.rol = rol
        self.userName = userName
        self.password = password
        
class Patient():
    def __init__(self, id, name, dateBirth, gender, address, phoneNumber, email):
        self.id = id
        self.name = name
        self.dateBirth = dateBirth
        self.gender = gender
        self.address = address 
        self.phoneNumber = phoneNumber
        self.email = email
        
class EmergencyContact():
    def __init__(self, name, relationship, phoneNumber):
        self.name = name
        self.relationship = relationship
        self.phoneNumber = phoneNumber

class Insurance():
    def __init__(self, company, number, status, term):
        self.company = company
        self.number = number
        self.status = status
        self.term = term
