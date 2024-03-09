from .typeValidator import *
from service.rolServices import nurseServices

def addVisit(hospital):
    patientId = numberValidator(input("Ingrese el ID del paciente: " + "\n"), "Id del paciente")
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
        while True:
            orderMedication = input("- Ingrese la orden a la que pertenecen los medicamentos aplicados al paciente: - " + "\n")
            if nurseServices.checkOrderById(hospital, orderMedication):
                numberValidator(orderMedication, "Orden de medicamentos del paciente")
                break
            else:
                print("La orden ingresada no es válida.")

    procedures = input("Ingrese los procedimientos del paciente: " + "\n")
    if procedures == "":
        procedures = "N/A"
    textValidator(procedures, "Procedimientos del paciente")
    orderProcedure = None 
    if procedures != "N/A":
        while True:
            orderProcedure = input("- Ingrese la orden a la que pertenece el procedimiento hecho al paciente: - " + "\n")
            if nurseServices.checkOrderById(hospital, orderProcedure):
                numberValidator(orderProcedure, "Orden de procedimientos del paciente")
                break
            else:
                print("La orden ingresada no es válida.")

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

def patientOrders(hospital):
    patientId = input("Ingrese el ID del paciente: " + "\n")
    orders = nurseServices.patientOrders(hospital, patientId)
    for order in orders:
        print("Order ID:", order.id)
        print("Patient ID:", order.patientId)
        print("Doctor ID:", order.doctorId)
        print("Date:", order.date)
        
        print("Medications:")
        for medication in order.orderMedication:
            for med in medication:
                print("- ID:", med.idMedication)
                print("  Dose:", med.dose)
                print("  Duration:", med.duration)
                print("  Amount:", med.amount)
                print("  Item:", med.item)
        
        print("Procedures:")
        for procedure in order.orderProcedure:
            for pro in procedure:
                print("- ID:", pro.idProcedure)
                print("  Amount:", pro.amount)
                print("  Frequency:", pro.frequency)
                print("  Special Assistance:", pro.specialAssistance)
                print("  Specialist ID:", pro.idSpecialist)
        
        print("Diagnostic Aids:")
        for orderDiagnosticAid in order.orderDiagnosticAid:
            print("- Name:", orderDiagnosticAid.nameDiagnosticAid)
            print("  Quantity:", orderDiagnosticAid.quantity)
            print("  Special Assistance:", orderDiagnosticAid.specialAssistance)
            print("  Specialist ID:", orderDiagnosticAid.idSpecialist)
        
        print("-" * 20 + "\n")