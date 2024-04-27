from .typeValidator import *
from HospitalApp.service import doctorService

# --------- GET
def getMedicalRecords(patientId):
    patientId = numberValidator(patientId, "Id de paciente")
    return doctorService.getMedicalRecords(patientId)


def getBasicInfoPatient(patientId):
    patientId = numberValidator(patientId, "Id de paciente")
    return doctorService.getBasicInfoPatient(patientId)


# --------- POST
def createMedicalRecord(patientId, idDoctor, consultationReason, symptoms, diagnosis, order):
    patientId = numberValidator(patientId, "Id de paciente")
    idDoctor = numberValidator(idDoctor, "Id de doctor")
    consultationReason = textValidator(consultationReason, "Motivo de consulta")
    symptoms = textValidator(symptoms, "Síntomas")
    diagnosis = textValidator(diagnosis, "Diagnóstico")
    order = textValidator(order, "Orden")
    doctorService.createMedicalRecord(patientId, idDoctor, consultationReason, symptoms, diagnosis, order)
