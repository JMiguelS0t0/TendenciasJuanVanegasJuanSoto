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
    def __init__(self, id, patientId, date, bloodPressure, temperature, pulse, oxygenLvl, medications, procedures, observations):
        self.patientId = patientId
        self.date = date
        self.bloodPressure = bloodPressure
        self.temperature = temperature
        self.pulse = pulse
        self.oxygenLvl = oxygenLvl
        self.medications = medications
        self.procedures = procedures
        self.observations = observations
class MedicalRecord():
    def __init__(self, idPatient, date, idDoctor, reasonConsulta, symptoms, diagnosis):
        self.idPatient = idPatient
        self.date = date
        self.idDoctor = idDoctor
        self.reasonConsulta = reasonConsulta
        self.symptoms = symptoms
        self.diagnosis = diagnosis

class Medications():
    def __init__(self, id, idMedication, dose, duration, item, price):
        self.id = id
        self.idMedication = idMedication
        self.dose = dose
        self.duration = duration
        self.item = item
        self.price = price

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


class Hospital():
    def __init__(self):
        self.persons = []
        self.patients = []
        self.emergencyContacts = []
        self.insurances = []
        self.appointments = []
        self.visits = {}        