from django.forms import model_to_dict
import HospitalApp.validators.administrativePersonnelValidator as APValidator
from django.http.response import JsonResponse
import json


# ----------- PATIENT
def getPatient(self, request, id = None):
    try:
        patients = [APValidator.getPatient(id)] if id else APValidator.getPatients()
        patientsData = [
            {
                "id": patient.id,
                "name": patient.name,
                "dateBirth": patient.dateBirth,
                "gender": patient.gender,
                "address": patient.address,
                "phoneNumber": patient.phoneNumber,
                "email": patient.email
            } for patient in patients
        ]
        status = 200 if patientsData else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(patientsData, status=status, safe=False)
            
def postPatient(self, request):
    try:
        body = json.loads(request.body)
        idNumber = body["idNumber"]
        name = body["name"]
        dateBirth = body["dateBirth"]
        gender = body["gender"]
        address = body["address"]
        phoneNumber = body["phoneNumber"]
        email = body["email"]
        APValidator.createPatient(idNumber, name, dateBirth, gender, address, phoneNumber, email)
        message = "Paciente creado exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status = status) 

def putPatient(self, request, id = None):
    try:
        body = json.loads(request.body)
        APValidator.updatePatient(
            id, 
            body.get("name"),
            body.get("dateBirth"),
            body.get("gender"),
            body.get("address"),
            body.get("phoneNumber"),
            body.get("email")
        )
        message = "Paciente actualizado exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)


def deletePatient(self, request, id = None):
    try:
        APValidator.deletePatient(id)
        message = "Paciente eliminado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    
    response = {"message": message}
    return JsonResponse(response, status = status)

# ----------- CONTACT

def postContact(self, request):
    try:
        body = json.loads(request.body)
        idUser = body["idUser"]
        name = body["name"]
        relationship = body["relationship"]
        phoneNumber = body["phoneNumber"]
        patientInstance = APValidator.patientInstance(idUser)
        APValidator.createContact(patientInstance, name, relationship, phoneNumber)
        message = "Contacto agregado exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status = status) 

def getContact(self, request, id=None):
    try:
        contacts = [APValidator.getContact(id)] if id else APValidator.getContacts()
        contactData = [
            {
                "idUser": contact.idUser,
                "name": contact.name,
                "relationship": contact.relationship,
                "phoneNumber": contact.phoneNumber
            } for contact in contacts
        ]
        status = 200 if contactData else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        contactData = [model_to_dict(contact) for contact in contacts]  # Convertir los objetos Patient a diccionarios antes de serializarlos a JSON
        return JsonResponse(contactData, status=status, safe=False)

def putContact(self, request, id=None):
    try:
        body = json.loads(request.body)
        idUser = body.get("idUser")
        name = body.get("name")
        relationship = body.get("relationship")
        phoneNumber = body.get("phoneNumber")

        patientInstance = APValidator.patientInstance(idUser)

        APValidator.updateContact(
            patientInstance,
            name,
            relationship,
            phoneNumber
        )

        message = "Contacto actualizado exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400

    response = {"message": message}
    return JsonResponse(response, status=status)


def deleteContact(self, request, id = None):
    try:
        APValidator.deleteContact(id)
        message = "Contacto eliminado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    
    response = {"message": message}
    return JsonResponse(response, status = status)


# ----------- INSURANCE

def postInsurance(self, request):
    try:
        body = json.loads(request.body)
        idUser = body["idUser"]
        company = body["company"]
        number = body["number"]
        status = body["status"]
        term = body["term"]
        patientInstance = APValidator.patientInstance(idUser)
        APValidator.createInsurance(patientInstance, company, number, status, term)
        message = "Seguro agregado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status = status) 

def getInsurance(self, request, id=None):
    try:
        insurances = [APValidator.getInsurance(id)] if id else APValidator.getInsurances()
        insuranceData = [
            {
            "idUser": insurance.idUser,
            "company": insurance.company,
            "number": insurance.number,
            "status": insurance.status,
            "term": insurance.term
            } for insurance in insurances
        ]
        status = 200 if insuranceData else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        insuranceData = [model_to_dict(insurance) for insurance in insurances]  # Convertir los objetos Patient a diccionarios antes de serializarlos a JSON
        return JsonResponse(insuranceData, status=status, safe=False)

def putInsurance(self, request, id=None):
    try:
        body = json.loads(request.body)
        idUser = body.get("idUser")
        company = body.get("company")
        number = body.get("number")
        status = body.get("status")
        term = body.get("term")

        patientInstance = APValidator.patientInstance(idUser)

        APValidator.updateInsurance(
            patientInstance,
            company,
            number,
            status,
            term
        )

        message = "Seguro actualizado exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400

    response = {"message": message}
    return JsonResponse(response, status=status)


def deleteInsurance(self, request, id = None):
    try:
        APValidator.deleteInsurance(id)
        message = "Seguro eliminado exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    
    response = {"message": message}
    return JsonResponse(response, status = status)

# ----------- APPOINTMENT

def postAppointment(self, request):
    try:
        body = json.loads(request.body)
        idPatient = body["idPatient"]
        doctor = body["doctor"]
        date = body["date"]
        reason = body["reason"]
        patientInstance = APValidator.patientInstance(idPatient)
        doctorInstance = APValidator.doctorInstance(doctor)
        APValidator.createAppointment(patientInstance, doctorInstance, date, reason)
        message = "Cita creada exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status = status)

def getAppointment(self, request, id = None):
    try:
        appointments = APValidator.getAppointmentById(id)
        appointmentData = [
            {
            "id": appointment.id,
            "idPatient": appointment.idPatient,
            "doctor": appointment.doctor,
            "date": appointment.date,
            "reason": appointment.reason
            } for appointment in appointments
        ]
        status = 200 if appointmentData else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        appointmentData = [model_to_dict(appointment) for appointment in appointments]  # Convertir los objetos Patient a diccionarios antes de serializarlos a JSON
        return JsonResponse(appointmentData, status=status, safe=False)

def deleteAppointment(self, request, id = None):
    try:
        body = json.loads(request.body)
        date = body["date"]
        APValidator.deleteAppointment(id, date)
        message = "Cita eliminada exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    
    response = {"message": message}
    return JsonResponse(response, status = status)