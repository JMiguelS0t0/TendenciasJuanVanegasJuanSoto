import model.models as models
from .administrativePersonnelServices import getPatientById
import datetime

def addMedicalRecord(hospital, patientId, idDoctor, consultationReason, symptoms, diagnosis, diagnosisAid, medications, procedures):
    patient = getPatientById(hospital, str(patientId))
    if patient is None:
        raise Exception("El paciente no existe")
    date = datetime.date.today()
    newClinicalHistory = {}
    newClinicalHistory["date"] = date
    newClinicalHistory["idDoctor"] = idDoctor
    newClinicalHistory["consultationReason"] = consultationReason
    newClinicalHistory["symptoms"] = symptoms
    newClinicalHistory["diagnosis"] = diagnosis
    if diagnosisAid != "N/A":
        order = models.Order(len(hospital.orders), patient.id, date, "N/A", "N/A", diagnosisAid)
        hospital.orders.append(order)
    if diagnosisAid == "N/A":
        newClinicalHistory["medications"] = medications
        newClinicalHistory["procedures"] = procedures
        order = models.Order(len(hospital.orders), patient.id, date, medications, procedures, "N/A")
        hospital.orders.append(order)
    if date not in hospital.clinicalHistory[str(patient.id)]:
        hospital.clinicalHistory[str(patient.id)][date] = {}
    hospital.clinicalHistory[str(patient.id)][date] = newClinicalHistory
    print("Historia clinica agregada con exito")
    print(hospital.clinicalHistory)

    for key, value in newClinicalHistory.items():
        print(f"{key}: {value}")
    print(hospital.clinicalHistory[str(patientId)][date])
        
def updateMedicalRecord(hospital):
    pass