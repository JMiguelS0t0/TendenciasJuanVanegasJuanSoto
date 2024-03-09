from service.rolServices import doctorServices
from service.rolServices.administrativePersonnelServices import getPatientById
from .typeValidator import *

def addMedicalRecord(hospital, idDoctor):
    patientId = numberValidator(input("Ingrese el ID del paciente: " + "\n"), "Id del paciente")
    try:
        patient = getPatientById(hospital, patientId)
        if patient is None:
            raise ValueError("No existe el paciente. Ingrese nuevamente el ID")
    except ValueError as e:
        print(str(e))
        return 
    consultationReason = textValidator(input("Ingrese el motivo de la consulta: " + "\n"), "Motivo de la consulta")
    symptoms = textValidator(input("Ingrese los sintomas del paciente: " + "\n"), "Sintomas del paciente")
    diagnosis = textValidator(input("Ingrese el diagnostico del paciente: " + "\n"), "Diagnostico del paciente")
    medications = []
    procedures = []
    lastOrderId = len(hospital.orders) + 1
    

    try:
        if askYesNoQuestion("Va a solicitar una ayuda diagnostica?"):
            diagnosticAid = addDiagnosisAidOrder(lastOrderId)
        else:
            diagnosticAid = "N/A"
    except ValueError as e:
        print(str(e))

    if diagnosticAid == "N/A":
        try:
            if askYesNoQuestion("Va a agregar un medicamento?"):
                while True:
                    medication = addMedicationOrder(hospital, lastOrderId)
                    medications.append(medication)
                    if not askYesNoQuestion("¿Desea agregar otro medicamento?"):
                        break
            else:
                medications = "N/A"
        except ValueError as e:
            print(str(e))

        try:
            if askYesNoQuestion("Va a agregar un procedimiento?"):
                while True:
                    procedure = addProcedureOrder(lastOrderId)
                    procedures.append(procedure)
                    if not askYesNoQuestion("¿Desea agregar otro procedimiento?"):
                        break
            else:
                procedures = "N/A"
        except ValueError as e:
            print(str(e))

    doctorServices.addMedicalRecord(hospital, patientId, idDoctor, consultationReason, symptoms, diagnosis, diagnosticAid, medications, procedures)

def addDiagnosisAidOrder(idOrder):
    nameDiagnosticAid = textValidator(input("Ingrese el nombre de la ayuda diagnostica: " + "\n"), "Nombre de la ayuda diagnostica")
    quantity = numberValidator(input("Ingrese la cantidad de la ayuda diagnostica: " + "\n"), "Cantidad de la ayuda diagnostica")
    while True:
        try:
            answer = input("¿Necesita asistencia especial? (Si/No): ").lower()
            if answer == "si":
                specialAssistance = True
                break
            elif answer == "no":
                specialAssistance = False
                break
            else:
                print("Opcion incorrecta. Por favor ingrese 'Si' o 'No'.")
        except ValueError as e:
            print(str(e))
    if specialAssistance:
        idSpecialist = numberValidator(input("Ingrese el ID del especialista: " + "\n"), "Id del especialista")
    else:
        idSpecialist = None
    diagnosticAid = doctorServices.addDiagnosisAidOrder(idOrder, nameDiagnosticAid, quantity, specialAssistance, idSpecialist)
    return diagnosticAid

def addMedicationOrder(idOrder):
    idMedication = numberValidator(input("Ingrese el ID del medicamento: " + "\n"), "Id del medicamento")
    dose = textValidator(input("Ingrese la dosis del medicamento: " + "\n"), "Dosis del medicamento")
    duration = textValidator(input("Ingrese la duracion del medicamento: " + "\n"), "Duracion del medicamento")
    amount = numberValidator(input("Ingrese la cantidad del medicamento: " + "\n"), "Cantidad del medicamento")
    item = input("Ingrese el item del medicamento: " + "\n")
    medication = doctorServices.addMedicationOrder(idOrder, idMedication, dose, duration, amount, item)  
    return medication


def addProcedureOrder(idOrder):
    idProcedure = numberValidator(input("Ingrese el ID del procedimiento: " + "\n"), "Id del procedimiento")
    amount = numberValidator(input("Ingrese la cantidad del procedimiento: " + "\n"), "Cantidad del procedimiento")
    frequency = textValidator(input("Ingrese la frecuencia del procedimiento: " + "\n"), "Frecuencia del procedimiento")
    while True:
        try:
            answer = input("¿Necesita asistencia especial? (Si/No): ").lower()
            if answer == "si":
                specialAssistance = True
                break
            elif answer == "no":
                specialAssistance = False
                break
            else:
                print("Opcion incorrecta. Por favor ingrese 'Si' o 'No'.")
        except ValueError as e:
            print(str(e))
    if specialAssistance:
        idSpecialist = numberValidator(input("Ingrese el ID del especialista: " + "\n"), "Id del especialista")
    else:
        idSpecialist = None
    procedure = doctorServices.addProcedureOrder(idOrder, idProcedure, amount, frequency, specialAssistance, idSpecialist)
    return procedure

def askYesNoQuestion(question):
    while True:
        try:
            print(question + " (Si/No)")
            answer = input()
            if answer.lower() == "si":
                return True
            elif answer.lower() == "no":
                return False
            else:
                raise ValueError("Opcion incorrecta. Por favor ingrese 'Si' o 'No'.")
        except ValueError as e:
            print(str(e))