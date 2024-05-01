from .typeValidator import *
from HospitalApp.service import doctorService

def getBasicInfoPatient(patientId):
    patientId = numberValidator(patientId, "Id de paciente")
    return doctorService.getBasicInfoPatient(patientId)

def patientInstance(user):
    return doctorService.patientInstance(user)

def doctorInstance(user):
    return doctorService.personInstance(user)

def orderInstance(orderId):
    return doctorService.orderInstance(orderId)

def medicationInstance(medicationId):
    return doctorService.medicationInstance(medicationId)

# ------------------------------------- MEDICAL RECORDS
# --------- GET
def getMedicalRecords(patientId):
    patientId = numberValidator(patientId, "Id de paciente")
    return doctorService.getMedicalRecords(patientId)

# --------- POST
def createMedicalRecord(patientId, idDoctor, consultationReason, symptoms, diagnosis):
    patientId = numberValidator(patientId, "Id de paciente")
    idDoctor = numberValidator(idDoctor, "Id de doctor")
    consultationReason = textValidator(consultationReason, "Motivo de consulta")
    symptoms = textValidator(symptoms, "Síntomas")
    diagnosis = textValidator(diagnosis, "Diagnóstico")
    doctorService.createMedicalRecord(patientId, idDoctor, consultationReason, symptoms, diagnosis)

# ------------------------------------- ORDERS
# --------- GET
def getOrdersByPatient(idPatient):
    idPatient = numberValidator(idPatient, "Id de paciente")
    return doctorService.getOrdersByPatient(idPatient)

# --------- POST
def createOrder(patientId, doctorId):
    patientId = numberValidator(patientId, "Id de paciente")
    doctorId = numberValidator(doctorId, "Id de doctor")
    doctorService.generateOrder(patientId, doctorId)

def createOrderMedication(idOrder, idMedication, dose, duration, amount):
    idOrder = numberValidator(idOrder, "Id de orden")
    idMedication = numberValidator(idMedication, "Id de medicamento")
    dose = textValidator(dose, "Dosis")
    duration = textValidator(duration, "Duración")
    amount = textValidator(amount, "Cantidad")
    doctorService.generateOrderMedication(idOrder, idMedication, dose, duration, amount)

def createOrderProcedure(idOrder, idProcedure, amount, frequency, specialAssistance, idSpecialist):
    idOrder = numberValidator(idOrder, "Id de orden")
    idProcedure = numberValidator(idProcedure, "Id de procedimiento")
    amount = textValidator(amount, "Cantidad")
    frequency = textValidator(frequency, "Frecuencia")
    specialAssistance = booleanValidator(specialAssistance, "Asistencia especial")
    idSpecialist = numberValidator(idSpecialist, "Id de especialista")
    doctorService.generateOrderProcedure(idOrder, idProcedure, amount, frequency, specialAssistance, idSpecialist)

def createOrderDiagnosticAid(orderId, diagnosticAidId, quantity, specialAssistance, idSpecialist):
    orderId = numberValidator(orderId, "Id de orden")
    diagnosticAidId = numberValidator(diagnosticAidId, "Id de ayuda diagnóstica")
    quantity = textValidator(quantity, "Cantidad")
    specialAssistance = booleanValidator(specialAssistance, "Asistencia especial")
    idSpecialist = numberValidator(idSpecialist, "Id de especialista")
    doctorService.generateOrderDiagnosticAid(orderId, diagnosticAidId, quantity, specialAssistance, idSpecialist)