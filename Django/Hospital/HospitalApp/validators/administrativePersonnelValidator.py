from .typeValidator import *
from HospitalApp.service import administrativePersonnelServices as APService


# ------------------------------------------------- OTHERS

def patientInstance(user):
    return APService.patientInstance(user)

def doctorInstance(user):
    return APService.doctorInstance(user)

# --------------------------------------------------------- PATIENT
# --------- POST
def createPatient(id, name, dateBirth, gender, address, phoneNumber, email):
    id = numberValidator(id, "Cedula del paciente")
    name = textValidator(name, "Nombre del paciente")
    dateBirth = dateBirthValidator(dateBirth, "Fecha de nacimiento del paciente")
    phoneNumber = phoneNumberValidator(phoneNumber, "Numero del paciente")
    email = emailValidator(email, "Email del paciente")
    APService.createPacient(id, name, dateBirth, gender, address, phoneNumber, email)

# --------- GET
def getPatient(id):
    id = numberValidator(id, "Cedula del paciente")
    return APService.getPatient(id)

def getPatients():
    return APService.getPatients()

# --------- DELETE
def deletePatient(id):
    return APService.deletePatient(id)

# --------- UPDATE
def updatePatient(id, name, dateBirth, gender, address, phoneNumber, email):
    id = numberValidator(id, "Cedula del paciente")
    name = textValidator(name, "Nombre del paciente")
    dateBirth = dateBirthValidator(dateBirth, "Fecha de nacimiento del paciente")
    phoneNumber = phoneNumberValidator(phoneNumber, "Numero del paciente")
    email = emailValidator(email, "Email del paciente")
    return APService.updatePatient(id, name, dateBirth, gender, address, phoneNumber, email)



# --------------------------------------------------------- EMERGENCY CONTACT
# --------- POST
def createContact(idUser, name, relationship, phoneNumber):
    idUser = numberValidator(idUser.id, "Cedula del paciente")
    name = textValidator(name, "Nombre del contacto de emergencia")
    phoneNumber = phoneNumberValidator(phoneNumber, "Numero del contacto de emergencia")
    idPatientInstance = patientInstance(idUser)
    APService.createContact(idPatientInstance, name, relationship, phoneNumber)

# --------- GET
def getContact(id):
    id = numberValidator(id, "Cedula del paciente")
    return APService.getContact(id)

def getContacts():
    return APService.getContacts()

# --------- DELETE
def deleteContact(id):
    return APService.deleteContact(id)

# --------- UPDATE
def updateContact(idUser, name, relationship, phoneNumber):
    name = textValidator(name, "Nombre del contacto")
    relationship = textValidator(relationship, "Relacion con el paciente")
    phoneNumber = phoneNumberValidator(phoneNumber, "Numero del contacto")
    return APService.updateContact(idUser, name, relationship, phoneNumber)


# --------------------------------------------------------- INSURANCE
# --------- POST
def createInsurance(idUser, company, number, status, term):
    idUser = numberValidator(idUser.id, "Cedula del paciente")
    company = textValidator(company, "Nombre de la compañía")
    number = numberValidator(number, "Número de póliza")
    status = textValidator(status, "Estado")
    term = textValidator(term, "Término")
    idPatientInstance = patientInstance(idUser)
    APService.createInsurance(idPatientInstance, company, number, status, term)

# --------- GET
def getInsurance(id):
    id = numberValidator(id, "Cedula del paciente")
    return APService.getInsurance(id)

def getInsurances():
    return APService.getInsurances()

# --------- DELETE
def deleteInsurance(id):
    return APService.deleteInsurance(id)

# --------- UPDATE
def updateInsurance(idUser, company, number, status, term):
    company = textValidator(company, "Nombre de la compañía")
    number = numberValidator(number, "Número de póliza")
    status = textValidator(status, "Estado")
    term = textValidator(term, "Término")
    return APService.updateInsurance(idUser, company, number, status, term)

# --------------------------------------------------------- APPOINTMENTS

# --------- POST
def createAppointment(idPatient, doctor, date, reason):
    idPatient = numberValidator(idPatient.id, "Cedula del paciente")
    doctor = numberValidator(doctor.cedula, "Cedula del doctor")
    date = validateDateFormat(date, "Fecha de la cita")
    reason = textValidator(reason, "Razon de la cita")
    idPatientInstance = patientInstance(idPatient)
    idDoctorInstance = doctorInstance(doctor)
    APService.createAppointment(idPatientInstance, idDoctorInstance, date, reason)

# --------- GET
def getAppointmentById(id):
    id = numberValidator(id, "Cedula del paciente")
    return APService.getAppointmentsByUserId(id)

# --------- DELETE
def deleteAppointment(patientId, date):
    patientId = numberValidator(patientId, "Cedula del paciente")
    date = validateDateFormat(date, "Fecha de la cita")
    return APService.deleteAppointment(patientId, date)

