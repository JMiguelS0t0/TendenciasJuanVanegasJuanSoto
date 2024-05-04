from HospitalApp import models
from Hospital.conection_mongo import collection

# ------------------------------------- PATIENTS
# --------- POST
def createPacient(id, name, dateBirth, gender, address, phoneNumber, email):
    patient = models.Patient.objects.filter(id = id)
    if patient.exists():
        raise Exception ("Ya existe un paciente con esa cedula")
    patient = None
    patient = models.Patient(id, name, dateBirth, gender, address, phoneNumber, email)
    patient.save()
    clinicalHistory = {"_id": str(patient.id), "historias": {}}
    collection.insert_one(clinicalHistory)

# --------- GET
def getPatient(id):
    try:
        patient = models.Patient.objects.filter(id = id).first()
        if patient:
            return patient
        else:
            raise Exception("El paciente no existe, ingrese una cedula valida")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener el usuario: " + str(e))

def getPatients():
    try:
        patients = models.Patient.objects.all()
        if patients:
            return patients
        else:
            raise Exception("No hay pacientes registrados")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener los pacientes: " + str(e))

# --------- DELETE
def deletePatient(id):
    try:
        patient = models.Patient.objects.filter(id = id).first()
        if patient:
            patient.delete()
        else:
            raise Exception("El paciente no existe, ingrese una cedula valida")
    except Exception as e:
        raise Exception("Ocurrio un error al eliminar el paciente: " + str(e))

# --------- PUT
def updatePatient(id, name, dateBirth, gender, address, phoneNumber, email):
    patient = models.Patient.objects.filter(id = id).first()
    if patient:
        patient.name = name
        patient.dateBirth = dateBirth
        patient.gender = gender
        patient.address = address
        patient.phoneNumber = phoneNumber
        patient.email = email
        patient.save()
    else:
        raise Exception("No se encontró ningún paciente con la cédula proporcionada.")

# ------------------------------------- EMERGENCY CONTACTS
# --------- POST
def createContact(idUser, name, relationship, phoneNumber):
    contact = models.EmergencyContact.objects.filter(idUser = idUser)
    if contact.exists():
        raise Exception ("Ya existe un contacto de emergencia para ese paciente")
    contact = None
    contact = models.EmergencyContact(idUser=idUser, name=name, relationship=relationship, phoneNumber=phoneNumber)
    contact.save()

# --------- GET
def getContact(id):
    try:
        contact = models.EmergencyContact.objects.filter(idUser = id).first()
        if contact:
            return contact
        else:
            raise Exception("El paciente no existe, ingrese una cedula valida")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener el usuario: " + str(e))

def getContacts():
    try:
        contacts = models.EmergencyContact.objects.all()
        if contacts:
            return contacts
        else:
            raise Exception("No hay contactos de emergencia registrados")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener los contactos: " + str(e))

# --------- DELETE
def deleteContact(id):
    try:
        contact = models.EmergencyContact.objects.filter(idUser = id).first()
        if contact:
            contact.delete()
        else:
            raise Exception("El contacto no existe, ingrese una cedula valida")
    except Exception as e:
        raise Exception("Ocurrio un error al eliminar el contacto: " + str(e))

# --------- PUT
def updateContact(idUser, name, relationship, phoneNumber):
    contact = models.EmergencyContact.objects.filter(idUser = idUser).first()
    if contact:
        contact.idUser = idUser
        contact.name = name
        contact.relationship = relationship
        contact.phoneNumber = phoneNumber
        contact.save()
    else:
        raise Exception("No se encontró ningún contacto con la cédula proporcionada.")


# ------------------------------------- INSURANCE
# --------- POST
def createInsurance(idUser, company, number, status, term):
    insurance = models.Insurance.objects.filter(idUser = idUser)
    if insurance.exists():
        raise Exception ("Ya existe un seguro para ese paciente")
    insurance = None
    insurance = models.Insurance(idUser=idUser, company=company, number=number, status=status, term=term)
    insurance.save()
# --------- GET
def getInsurance(id):
    try:
        insurance = models.Insurance.objects.filter(idUser = id).first()
        if insurance:
            return insurance
        else:
            raise Exception("El paciente no existe, ingrese una cedula valida")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener el usuario: " + str(e))

def getInsurances():
    try:
        insurances = models.Insurance.objects.all()
        if insurances:
            return insurances
        else:
            raise Exception("No hay seguros registrados")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener los seguros: " + str(e))
# --------- DELETE
def deleteInsurance(id):
    try:
        insurance = models.Insurance.objects.filter(idUser = id).first()
        if insurance:
            insurance.delete()
        else:
            raise Exception("El seguro no existe, ingrese una cedula valida")
    except Exception as e:
        raise Exception("Ocurrio un error al eliminar el seguro: " + str(e))

# --------- PUT
def updateInsurance(idUser, company, number, status, term):
    insurance = models.Insurance.objects.filter(idUser = idUser).first()
    if insurance:
        insurance.idUser = idUser
        insurance.company = company
        insurance.number = number
        insurance.status = status
        insurance.term = term
        insurance.save()
    else:
        raise Exception("No se encontró ningún seguro con la cédula proporcionada.")


# ------------------------------------- APPOINTMENTS
# --------- POST

def createAppointment(idPatient, doctor, date, reason):
    appointment = models.Appointment(idPatient = idPatient, doctor = doctor, date = date, reason = reason)
    appointment.save()

# --------- GET
def getAppointmentsByUserId(id):
    try:
        appointments = models.Appointment.objects.filter(idPatient = id)
        if appointments:
            return appointments
        else:
            raise Exception("No se encontraron citas para el paciente.")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener las citas del usuario." + str(e))

def deleteAppointment(patientid, date):
    try:
        appointment = models.Appointment.objects.filter(idPatient = patientid, date = date).first()
        if appointment:
            appointment.delete()
        else:
            raise Exception("La cita no existe, ingrese valores validos" + str(e))
    except Exception as e:
        raise Exception("Ocurrio un error al eliminar la cita: " + str(e))