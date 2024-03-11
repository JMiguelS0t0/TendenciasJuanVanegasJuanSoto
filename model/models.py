class Person():
    def __init__(self, name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password):
        self.name = name
        self.cedula = cedula
        self.email = email
        self.phoneNumber = phoneNumber
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
        self.emergencyContact = EmergencyContact
        self.insurance = Insurance
        
class EmergencyContact():
    def __init__(self, idUser, name, relationship, phoneNumber):
        self.idUser = idUser
        self.name = name
        self.relationship = relationship
        self.phoneNumber = phoneNumber

class Insurance():
    def __init__(self, idUser, company, number, status, term):
        self.idUser = idUser
        self.company = company
        self.number = number
        self.status = status
        self.term = term

class Appointment():
    def __init__(self, id, idPatient, doctorName, date, reason):
        self.id = id
        self.idPatient = idPatient
        self.doctorName = doctorName
        self.date = date
        self.reason = reason

class Visit():
    def __init__(self, patientId, date, bloodPressure, temperature, pulse, oxygenLvl, medications, orderMedication, procedures, orderProcedure, observations):
        self.patientId = patientId
        self.date = date
        self.bloodPressure = bloodPressure
        self.temperature = temperature
        self.pulse = pulse
        self.oxygenLvl = oxygenLvl
        self.medications = medications
        self.orderMedication = orderMedication
        self.procedures = procedures
        self.orderProcedure = orderProcedure
        self.observations = observations

class Medications():
    def __init__(self, id, idMedication, dose, duration, item):
        self.id = id
        self.idMedication = idMedication
        self.dose = dose
        self.duration = duration
        self.item = item

class Procedure():
    def __init__(self, id, idProcedure, quantity, frequency, reqAssistance, idSpecialist, item):
        self.id = id
        self.idProcedure = idProcedure
        self.quantity = quantity
        self.frequency = frequency
        self.reqAssistance = reqAssistance
        self.idSpecialist = idSpecialist
        self.item = item

class DiagnosticAid():
    def __init__(self, id, idDiagnosticAid, quantity, reqAssistance, idSpecialist, item):
        self.id = id
        self.idDiagnosticAid = idDiagnosticAid
        self.quantity = quantity
        self.reqAssistance = reqAssistance
        self.idSpecialist = idSpecialist
        self.item = item

class Invoice():
    def __init__(self, doctorName, diagnosis, medications, procedures, diagnosticTest):
        self.patient = Patient
        self.doctorName = doctorName
        self.diagnosis = diagnosis
        self.insuranceData = Insurance
        self.medications = medications
        self.procedures = procedures
        self.diagnosticTest = diagnosticTest

class Order():
    def __init__(self, id, patientId, doctorId, date):
        self.id = id
        self.patientId = patientId
        self.doctorId = doctorId
        self.date = date
        self.orderMedication = []
        self.orderProcedure = []
        self.orderDiagnosticAid = []
        
class OrderMedication():
    def __init__(self, idOrder, idMedication, dose, duration, amount):
        self.idOrder = idOrder
        self.idMedication = idMedication
        self.dose = dose
        self.duration = duration
        self.amount = amount

class orderProcedure():
    def __init__(self, idOrder, idProcedure, amount, frequency, specialAssistance, idSpecialist):
        self.idOrder = idOrder
        self.idProcedure = idProcedure
        self.amount = amount
        self.frequency = frequency
        self.specialAssistance = specialAssistance
        self.idSpecialist = idSpecialist

class OrderDiagnosticAid():
    def __init__(self, idOrder, nameDiagnosticAid, quantity, specialAssistance, idSpecialist):
        self.idOrder = idOrder
        self.nameDiagnosticAid = nameDiagnosticAid
        self.quantity = quantity
        self.specialAssistance = specialAssistance
        self.idSpecialist = idSpecialist

class Hospital():
    def __init__(self):
        self.persons = []
        self.patients = []
        self.emergencyContacts = []
        self.insurances = []
        self.appointments = []
        self.visits = {}
        self.orders = []
        self.clinicalHistory = {}