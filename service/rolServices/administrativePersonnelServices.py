import model.models as models

def getPatientById(hospital, id):
    for patient in hospital.patients:
        if str(patient.id) == id:
            return patient
    return None

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

def updatePacient():
    pass

def deletePacient():
    pass

def scheduleAppointment():
    pass

def invoice():
    pass

def validateId(hospital, id):
    for patient in hospital.patients:
        if patient.id == id:
            return patient
    return None
