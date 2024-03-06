from .typeValidator import *
from service.rolServices import nurseServices

def addVisit(hospital):
    patientId = input("Ingrese el ID del paciente: " + "\n")
    bloodPressure = numberValidator(input("Ingrese la presion sanguinea del paciente: " + "\n"), "Presion sanguinea del paciente")
    temperature = numberValidator(input("Ingrese la temperatura del paciente: " + "\n"), "Temperatura del paciente")
    pulse = numberValidator(input("Ingrese el pulso del paciente: " + "\n"), "Pulso del paciente")
    oxygenLvl = numberValidator(input("Ingrese el nivel de oxigeno del paciente: " + "\n"), "Nivel de oxigeno del paciente")
    medications = input("Ingrese los medicamentos del paciente: " + "\n")

    if medications == "":
        medications = "N/A"
    textValidator(medications, "Medicamentos del paciente")
    orderMedication = None
    if medications != "N/A":
        orderMedication = input("- Ingrese la orden a la que pertenecen los medicamentos aplicados al paciente: - " + "\n")
        textValidator(orderMedication, "Orden de medicamentos del paciente")

    procedures = input("Ingrese los procedimientos del paciente: " + "\n")
    if procedures == "":
        procedures = "N/A"
    textValidator(procedures, "Procedimientos del paciente")
    orderProcedure = None 
    if procedures != "N/A":
        orderProcedure = input("- Ingrese la orden a la que pertenece el procedimiento hecho al paciente: - " + "\n")
        textValidator(orderProcedure, "Orden de procedimientos del paciente")

    observations = input("Ingrese las observaciones del paciente: " + "\n")
    if observations == "":
        observations = "N/A"
    textValidator(observations, "Observaciones del paciente")
    nurseServices.addVisit(hospital, patientId, bloodPressure, temperature, pulse, oxygenLvl, medications, orderMedication, procedures, orderProcedure, observations)

def getVisitsById(hospital):
    patientId = input("Ingrese el ID del paciente: " + "\n")
    visits = nurseServices.getVisitsById(hospital, patientId)
    for visit in visits:
        print(visit)
        print("-" * 20 + "\n")