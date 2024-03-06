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
    if str(patient.id) not in hospital.clinicalHistory:
        hospital.clinicalHistory[str(patient.id)] = {}
    if date not in hospital.clinicalHistory[str(patient.id)]:
        hospital.clinicalHistory[str(patient.id)][date] = []
    hospital.clinicalHistory[str(patient.id)][date].append(newClinicalHistory)
    print("Historia clinica agregada con exito")
    print(hospital.clinicalHistory)

    # Show clinical history after creating it
    print("Historia clinica:")
    for patient_id, patient_history in hospital.clinicalHistory.items():
        print(f"Paciente ID: {patient_id}")
        for date, records in patient_history.items():
            print(f"Fecha: {date}")
            for record in records:
                print(f"Registro: {record}")
        
def updateMedicalRecord(hospital):
    pass