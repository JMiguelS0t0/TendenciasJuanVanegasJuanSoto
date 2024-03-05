import model.models as models

def getPatientById(hospital, id):
    for patient in hospital.patients:
        if str(patient.id) == id:
            return patient
    return None

# ------------------------------------- CREATE
def createPacient(hospital, id, name, dateBirth, gender, address, phoneNumber, email):
    patient = validateId(hospital, id)
    if patient:
        raise Exception("Ya existe una persona con esa cedula registrada")
    patient = models.Patient(id, name, dateBirth, gender, address, phoneNumber, email)
    hospital.patients.append(patient)
    # print(f"ID: {patient.id}")

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

def updatePacient(hospital, id, name=None, dateBirth=None, gender=None, address=None, phoneNumber=None, email=None):
    patient = getPatientById(hospital, id)
    if not patient:
        raise Exception("No existe una persona con esa cedula registrada")
    if name is not None:
        patient.name = name
    if dateBirth is not None:
        patient.dateBirth = dateBirth
    if gender is not None:
        patient.gender = gender
    if address is not None:
        patient.address = address
    if phoneNumber is not None:
        patient.phoneNumber = phoneNumber
    if email is not None:
        patient.email = email
    print("Datos del paciente actualizados correctamente.")
    
def updateEmergencyContact(hospital, idUser, name=None, relationship=None, phoneNumber=None):
    patient = getPatientById(hospital, idUser)
    if not patient:
        raise Exception("No existe una persona con esa cedula registrada")
    if name is not None:
        patient.emergencyContact.name = name
    if relationship is not None:
        patient.emergencyContact.relationship = relationship
    if phoneNumber is not None:
        patient.emergencyContact.phoneNumber = phoneNumber
    print("Datos del contacto de emergencia actualizados correctamente.")

def updateInsurance(hospital, idUser, company=None, number=None, status=None, term=None):
    patient = getPatientById(hospital, idUser)
    if not patient:
        raise Exception("No existe una persona con esa cedula registrada")
    if company is not None:
        patient.insurance.company = company
    if number is not None:
        patient.insurance.number = number
    if status is not None:
        patient.insurance.status = status
    if term is not None:
        patient.insurance.term = term
    print("Datos del seguro actualizados correctamente.")

<<<<<<< HEAD
def scheduleAppointment():
    pass

=======
# ----------------------------------------------- APPOINTMENTS
def scheduleAppointment(hospital, id, idPatient, date, reason):
    print("Cita agendada correctamente.")
    appointment = models.Appointment(id, idPatient, date, reason)
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
>>>>>>> 30393c8 (ADD - schedule/search Appointments)
def invoice():
    pass

def validateId(hospital, id):
    for patient in hospital.patients:
        if patient.id == id:
            return patient
    return None

def assignAppointmentId(hospital):
    if len(hospital.appointments) == 0:
        return 1
    else:
        lastId = hospital.appointments[-1].id
        return int(lastId) + 1