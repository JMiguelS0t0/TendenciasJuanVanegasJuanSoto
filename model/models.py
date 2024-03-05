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
        
class EmergencyContact():
    def __init__(self, name, relationship, phoneNumber):
        self.name = name
        self.relationship = relationship
        self.phoneNumber = phoneNumber

class Insurance():
<<<<<<< HEAD
    def __init__(self, company, number, status, term):
=======
    def __init__(self, idUser, company, number, status, term):
        self.idUser = idUser
>>>>>>> c8cb5a0 (ADD - UPDATE PATIENTS (EMERGENCYCONTACT & INSURANCE))
        self.company = company
        self.number = number
        self.status = status
        self.term = term

<<<<<<< HEAD
=======
class Appointment():
    def __init__(self, id, idPatient, date, reason):
        self.id = id
        self.idPatient = idPatient
        self.date = date
        self.reason = reason

>>>>>>> 30393c8 (ADD - schedule/search Appointments)
class Visit():
    def __init__(self, patient, date, bloodPressure, temperature, pulse, oxygenLvl, medicationsAdm, procedures, tests, observations):
        self.patient = patient
        self.date = date
        self.bloodPressure = bloodPressure
        self.temperature = temperature
        self.pulse = pulse
        self.oxygenLvl = oxygenLvl
        self.medicationsAdm = medicationsAdm
        self.procedures = procedures
        self.tests = tests
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
    def __init__(self, patient, diagnosis, medications, procedures, diagnosticTest):
        self.patient = patient
        self.diagnosis = diagnosis
        self.medications = medications
        self.procedures = procedures
        self.diagnosticTest = diagnosticTest


class Hospital():
    def __init__(self):
        self.persons = []
        self.patients = []
        self.invoices = []
        