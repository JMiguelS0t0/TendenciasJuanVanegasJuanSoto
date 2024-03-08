import model.models as models
from .administrativePersonnelServices import getPatientById
import datetime

def addMedicalRecord(hospital, patientId, idDoctor, consultationReason, symptoms, diagnosis, diagnosisAid, medications, procedures):
    patient = getPatientById(hospital, str(patientId))
    idOrder = len(hospital.orders) - 1

    if patient is None:
        raise Exception("El paciente no existe")

    date = datetime.date.today().strftime("%d/%m/%Y")
    newClinicalHistory = {}
    newClinicalHistory["date"] = date
    newClinicalHistory["idDoctor"] = idDoctor
    newClinicalHistory["consultationReason"] = consultationReason
    newClinicalHistory["symptoms"] = symptoms
    newClinicalHistory["diagnosis"] = diagnosis
    newClinicalHistory["order"] = None

    if diagnosisAid == "N/A" and medications == "N/A" and procedures == "N/A":
        hospital.clinicalHistory[str(patient.id)][date] = newClinicalHistory
        print(f"Historia clinica del paciente {patient.id} agregada con exito")
        return

    actualOrder = models.Order(idOrder, patient.id, idDoctor, date)
    if diagnosisAid != "N/A":
        actualOrder.orderDiagnosticAid.append(diagnosisAid)
        newClinicalHistory["order"] = actualOrder
        print(f"Ayuda diagnostica asignada a la orden: {actualOrder.id}")
        print(f"Historia clinica del paciente {patient.id} agregada.")
        
    if diagnosisAid == "N/A":
        if medications != "N/A":
            actualOrder.orderMedication.append(medications)
            newClinicalHistory["order"] = actualOrder
            print(f"Medicamento asignados a la orden: {actualOrder.id}")

        if procedures != "N/A":
            actualOrder.orderProcedure.append(procedures)
            newClinicalHistory["order"] = actualOrder
            print(f"Procedimiento asignados a la orden: {actualOrder.id}")

    hospital.orders.append(actualOrder)
    newClinicalHistory["order"] = actualOrder


    if date not in hospital.clinicalHistory[str(patient.id)]:
        hospital.clinicalHistory[str(patient.id)][date] = {}
    hospital.clinicalHistory[str(patient.id)][date] = newClinicalHistory
    print("Historia clinica agregada con exito")

    print("\n" + "----------- Historia clinica: -----------")
    for key, value in newClinicalHistory.items():
        print(f"{key}: {value}")
    
    print("\n" + "-----------Orden: -----------")
    for key, value in actualOrder.__dict__.items():
        print(f"{key}: {value}")

def createEmptyOrder(hospital):
    idOrder = len(hospital.orders)
    order = models.Order(idOrder, "N/A", "N/A", "N/A")
    hospital.orders.append(order)
    return order

def addDiagnosisAidOrder(hospital, idOrder, nameDiagnosticAid, quantity, amount, specialAssistance, idSpecialist):
    order = next((o for o in hospital.orders if o.id == idOrder), None)
    if order is None:
        raise Exception("La orden no existe")
    diagnosisAidOrder = models.OrderDiagnosticAid(idOrder, nameDiagnosticAid, quantity, amount, specialAssistance, idSpecialist)
    return diagnosisAidOrder

def addMedicationOrder(hospital, idOrder, idMedication, dose, duration, amount):
    order = next((o for o in hospital.orders if o.id == idOrder), None)
    if order is None:
        raise Exception("La orden no existe")
    medicationOrder = models.OrderMedication(idOrder, idMedication, dose, duration, amount)
    return medicationOrder
    
def addProcedureOrder(hospital, idOrder, idProcedure, amount, frequency, specialAssistance, idSpecialist):
    order = next((o for o in hospital.orders if o.id == idOrder), None)
    if order is None:
        raise Exception("La orden no existe")
    procedureOrder = models.orderProcedure(idOrder, idProcedure, amount, frequency, specialAssistance, idSpecialist)
    return procedureOrder

def updateMedicalRecord(hospital):
    pass

