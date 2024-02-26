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
