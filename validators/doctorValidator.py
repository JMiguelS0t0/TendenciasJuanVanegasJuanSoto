from service.rolServices import doctorServices
from .typeValidator import *

def addMedicalRecord(hospital):
    patientId = numberValidator(input("Ingrese el ID del paciente: " + "\n"), "Id del paciente")
    idDoctor = numberValidator(input("Ingrese el ID del doctor: " + "\n"), "Id del doctor")
    consultationReason = textValidator(input("Ingrese el motivo de la consulta: " + "\n"), "Motivo de la consulta")
    symptoms = textValidator(input("Ingrese los sintomas del paciente: " + "\n"), "Sintomas del paciente")
    diagnosis = textValidator(input("Ingrese el diagnostico del paciente: " + "\n"), "Diagnostico del paciente")
    medications = "N/A"
    procedures = "N/A"
    
    try:
        print("Va a solicitar una ayuda diagnostica? (Si/No)")
        answer = input()
        if answer.lower() == "si":
            diagnosticAid = textValidator(input("Ingrese la ayuda diagnostica solicitada: " + "\n"), "Ayuda diagnostica")
        elif answer.lower() == "no":
            diagnosticAid = "N/A"
        else:
            raise ValueError("Opcion incorrecta. Por favor ingrese 'Si' o 'No'.")
    except ValueError as e:
        print(str(e))
        diagnosticAid = "N/A"
            
    if diagnosticAid == "N/A":
        medications = textValidator(input("Ingrese los medicamentos del paciente: " + "\n"), "Medicamentos del paciente")
        procedures = textValidator(input("Ingrese los procedimientos del paciente: " + "\n"), "Procedimientos del paciente")
    
    doctorServices.addMedicalRecord(hospital, patientId, idDoctor, consultationReason, symptoms, diagnosis, diagnosticAid, medications, procedures)