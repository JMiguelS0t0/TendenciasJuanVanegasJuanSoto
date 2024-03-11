from .typeValidator import *
from service.rolServices import nurseServices

def addVisit(hospital):
    patientId = numberValidator(input("Ingrese el ID del paciente: \n"), "Id del paciente")
    bloodPressure = numberValidator(input("Ingrese la presion sanguinea del paciente: \n"), "Presion sanguinea del paciente")
    temperature = numberValidator(input("Ingrese la temperatura del paciente: \n"), "Temperatura del paciente")
    pulse = numberValidator(input("Ingrese el pulso del paciente: \n"), "Pulso del paciente")
    oxygenLvl = numberValidator(input("Ingrese el nivel de oxigeno del paciente: \n"), "Nivel de oxigeno del paciente")
    medications = input("Ingrese los medicamentos del paciente: \n")
    medications = "N/A" if medications == "" else medications
    textValidator(medications, "Medicamentos del paciente")
    orderMedication = None
    if medications != "N/A":
        orderMedication = getValidOrder(hospital, "Orden de medicamentos del paciente")
    
    procedures = input("Ingrese los procedimientos del paciente: \n")
    procedures = "N/A" if procedures == "" else procedures
    textValidator(procedures, "Procedimientos del paciente")
    orderProcedure = None
    if procedures != "N/A":
        orderProcedure = getValidOrder(hospital, "Orden de procedimientos del paciente")

    observations = input("Ingrese las observaciones del paciente: \n")
    observations = "N/A" if observations == "" else observations
    textValidator(observations, "Observaciones del paciente")
    nurseServices.addVisit(hospital, patientId, bloodPressure, temperature, pulse, oxygenLvl, medications, orderMedication, procedures, orderProcedure, observations)

def getValidOrder(hospital, message):
    while True:
        order = input("- " + message + ": - \n")
        try:
            numberValidator(order, message)
            if nurseServices.checkOrderById(hospital, order):
                return order
            else:
                print("La orden ingresada no es válida.")
        except ValueError:
            print("La orden ingresada no es válida. Debe ser un número entero.")


def getVisitsById(hospital):
    patientId = input("Ingrese el ID del paciente: " + "\n")
    visits = nurseServices.getVisitsById(hospital, patientId)
    for visit in visits:
        print(visit)
        print("-" * 20 + "\n")

def patientOrders(hospital):
    patientId = input("Ingrese el ID del paciente: \n")
    orders = nurseServices.patientOrders(hospital, patientId)
    for order in orders:
        print("Order ID:", order.id)
        print("Patient ID:", order.patientId)
        print("Doctor ID:", order.doctorId)
        print("Date:", order.date)
        print("Medications:")
        printMedications(order.orderMedication)
        print("Procedures:")
        printProcedures(order.orderProcedure)
        print("Diagnostic Aids:")
        printDiagnosticAids(order.orderDiagnosticAid)
        print("-" * 20 + "\n")

def printMedications(orderMedication):
    for medication in orderMedication:
        for med in medication:
            print("- ID:", med.idMedication)
            print("  Dose:", med.dose)
            print("  Duration:", med.duration)
            print("  Amount:", med.amount)
            print("  Item:", med.item)

def printProcedures(orderProcedure):
    for procedure in orderProcedure:
        for pro in procedure:
            print("- ID:", pro.idProcedure)
            print("  Amount:", pro.amount)
            print("  Frequency:", pro.frequency)
            print("  Special Assistance:", pro.specialAssistance)
            print("  Specialist ID:", pro.idSpecialist)
            print("  Item:", pro.item)

def printDiagnosticAids(orderDiagnosticAid):
    for orderDiagnosticAid in orderDiagnosticAid:
        print("- Name:", orderDiagnosticAid.nameDiagnosticAid)
        print("  Quantity:", orderDiagnosticAid.quantity)
        print("  Special Assistance:", orderDiagnosticAid.specialAssistance)
        print("  Specialist ID:", orderDiagnosticAid.idSpecialist)