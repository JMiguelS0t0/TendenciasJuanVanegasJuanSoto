import datetime
from HospitalApp import models
from Hospital.conection_mongo import collection

#TO DO: GET BASIC INFO PATIENTS, UPDATE MEDICAL RECORDS, ORDERS

def getMedicalRecords(patientId):
    try:
        patient = models.Patient.objects.get(id=patientId)
        patientIdStr = str(patient.id)
        clinicalHistory = collection.find_one({"_id": patientIdStr})

        if clinicalHistory:
            return clinicalHistory
        else:
            raise Exception("No se encontraron historias clínicas para el paciente")
    
    except models.Patient.DoesNotExist:
        raise Exception("El paciente no existe")

    except Exception as e:
        raise Exception("Ha ocurrido un error: " + str(e))

def createMedicalRecord(patientId, idDoctor, consultationReason, symptoms, diagnosis, order):
    patient = models.Patient.objects.get(id=patientId)
    patientIdStr = str(patient.id)
    medicalRecord = collection.find_one({"_id": patientIdStr})
    if medicalRecord is None:
        raise Exception("El paciente no tiene historial clínico")

    date = datetime.date.today().strftime("%d/%m/%Y")
    newClinicalHistory = {}
    newClinicalHistory["idDoctor"] = idDoctor
    newClinicalHistory["consultationReason"] = consultationReason
    newClinicalHistory["symptoms"] = symptoms
    newClinicalHistory["diagnosis"] = diagnosis
    newClinicalHistory["order"] = order

    if date in medicalRecord["historias"]:
        medicalRecord["historias"][date].append(newClinicalHistory)
    else:
        medicalRecord["historias"][date] = [newClinicalHistory]

    collection.update_one({"_id": patientIdStr}, {"$set": medicalRecord})

