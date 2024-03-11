import model.models as models

def getPatientById(hospital, id):
    for patient in hospital.patients:
        if str(patient.id) == str(id):
            return patient
    return None

# ------------------------------------- CREATE
def createPacient(hospital, id, name, dateBirth, gender, address, phoneNumber, email):
    patient = models.Patient(id, name, dateBirth, gender, address, phoneNumber, email)
    hospital.clinicalHistory[str(id)] = {}
    hospital.patients.append(patient)

def createEmergencyContact(hospital, idUser, name, relationship, phoneNumber):
    patient = next((p for p in hospital.patients if p.id == idUser), None)
    emergencyContact = models.EmergencyContact(idUser, name, relationship, phoneNumber)
    patient.emergencyContact = emergencyContact
    hospital.emergencyContacts.append(emergencyContact)
    
def createInsurance(hospital, idUser, company, number, status, term):
    patient = next((p for p in hospital.patients if p.id == idUser), None)
    insurance = models.Insurance(idUser, company, number, status, term)
    patient.insurance = insurance
    hospital.insurances.append(insurance)
    
# ------------------------------------- UPDATES
def updatePatient(hospital, id, name=None, dateBirth=None, gender=None, address=None, phoneNumber=None, email=None):
    patient = getPatientById(hospital, id)
    if not patient:
        raise Exception("No existe una persona con esa cedula registrada")
    if name != "No update":
        patient.name = name
    if dateBirth != "No Update" and dateBirth != None:
        patient.dateBirth = dateBirth
    if gender != "No update":
        patient.gender = gender
    if address != "No update":
        patient.address = address
    if phoneNumber != "No Update" and phoneNumber != None:
        patient.phoneNumber = phoneNumber
    if email != "No Update" and email != None:
        patient.email = email
    print("Datos del paciente actualizados correctamente.")
    
def updateEmergencyContact(hospital, idUser, name=None, relationship=None, phoneNumber=None):
    patient = getPatientById(hospital, idUser)
    if not patient:
        raise Exception("No existe una persona con esa cedula registrada")
    if name is not None and name != "No update":
        patient.emergencyContact.name = name
    if relationship is not None and relationship != "No update":
        patient.emergencyContact.relationship = relationship
    if phoneNumber is not None and phoneNumber != "No update":
        patient.emergencyContact.phoneNumber = phoneNumber
    print("Datos del contacto de emergencia actualizados correctamente.")

def updateInsurance(hospital, idUser, company=None, number=None, status=None, term=None):
    patient = getPatientById(hospital, idUser)
    if not patient:
        raise Exception("No existe una persona con esa cedula registrada")
    if company is not None and company != "No update":
        patient.insurance.company = company
    if number is not None and number != "No update":
        patient.insurance.number = number
    if status is not None and status != "No update":
        patient.insurance.status = status
    if term is not None and term != "No update":
        patient.insurance.term = term
    print("Datos del seguro actualizados correctamente.")

# ----------------------------------------------- APPOINTMENTS
def scheduleAppointment(hospital, id, idPatient, doctorName, date, reason):
    print("Cita agendada correctamente.")
    appointment = models.Appointment(id, idPatient, doctorName, date, reason)
    hospital.appointments.append(appointment)

def cancelAppointment():
    pass

def getAppointmentsByUserId(hospital, idUser):
    appointments = []
    for appointment in hospital.appointments:
        if appointment.idPatient == idUser:
            appointments.append(appointment)
    if appointments:
        return appointments
    else:
        print("No se encontraron citas para el paciente con ID {idUser}.")
        return

def searchAppointmentsByDay():
    pass

# ----------------------------------------------- INVOICE
def invoice():
    pass

def validateId(hospital, id):
    for patient in hospital.patients:
        if patient.id == str(id):
            return patient
    return None

def assignAppointmentId(hospital):
    if len(hospital.appointments) == 0:
        return 1
    else:
        lastId = hospital.appointments[-1].id
        return int(lastId) + 1