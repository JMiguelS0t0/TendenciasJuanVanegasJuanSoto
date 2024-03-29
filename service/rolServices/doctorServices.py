import model.models as models
from .administrativePersonnelServices import getPatientById
import datetime

def addMedicalRecord(hospital, patientId, idDoctor, consultationReason, symptoms, diagnosis, diagnosisAid, medications, procedures):
    patient = getPatientById(hospital, str(patientId))
    idOrder = len(hospital.orders) + 1
    actualOrder = models.Order(idOrder, patient.id, idDoctor, None)

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

    printClinicalHistory(newClinicalHistory, actualOrder)
    printOrderInfo(actualOrder)



def addDiagnosisAidOrder(idOrder, nameDiagnosticAid, quantity, specialAssistance, idSpecialist = None):
    diagnosisAidOrder = models.OrderDiagnosticAid(idOrder, nameDiagnosticAid, quantity, specialAssistance, idSpecialist)
    return diagnosisAidOrder

def addMedicationOrder(idOrder, idMedication, dose, duration, amount, cost, item):
    medicationOrder = models.OrderMedication(idOrder, idMedication, dose, duration, amount, cost, item)
    return medicationOrder
    
def addProcedureOrder(idOrder, idProcedure, amount, frequency, specialAssistance, idSpecialist = None, item = None):
    procedureOrder = models.orderProcedure(idOrder, idProcedure, amount, frequency, specialAssistance, idSpecialist, item)
    return procedureOrder


# -------------------------------- PRINTS

def printClinicalHistory(newClinicalHistory, actualOrder):
    print("\n" + "----------- Historia clinica: -----------")
    for key, value in newClinicalHistory.items():
        if key == "order":
            print(f"Orden asignada: {actualOrder.id}")
        else:
            print(f"{key}: {value}")

def printOrderInfo(actualOrder):
    print("\n" + "-----------Orden: -----------")
    for key, value in actualOrder.__dict__.items():
        if key == "orderDiagnosticAid":
            printDiagnosticAids(value)
        elif key == "orderMedication":
            printMedications(value)
        elif key == "orderProcedure":
            printProcedures(value)
        else:
            print(f"{key}: {value}")

def printDiagnosticAids(value):
    print("Ayudas diagnosticas:")
    for diagnosticAid in value:
        printItem(diagnosticAid)

def printMedications(value):
    print("Medicamentos:")
    for medication in value:
        printItem(medication)

def printProcedures(value):
    print("Procedimientos:")
    for procedure in value:
        printItem(procedure)

def printItem(item):
    if hasattr(item, '__dict__'):
        print(item.__dict__)
    else:
        print(item)

def getMedicationById(hospital, medicationId):
    for medication in hospital.medications:
        if medication.id == str(medicationId):
            return medication
    return None
    