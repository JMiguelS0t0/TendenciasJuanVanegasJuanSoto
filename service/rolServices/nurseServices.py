import model.models as models
from .administrativePersonnelServices import getPatientById
import datetime

def addVisit(hospital, patientId, bloodPressure, temperature, pulse, oxygenLvl, medications, orderMedication, procedures, orderProcedure, observations):
    patient = getPatientById(hospital, str(patientId))
    if patient is None:
        raise Exception("El paciente no existe")
    date = datetime.date.today().strftime("%d/%m/%Y")
    newVisit = {}
    newVisit["patientId"] = patient.id
    newVisit["date"] = date
    newVisit["bloodPressure"] = bloodPressure
    newVisit["temperature"] = temperature
    newVisit["pulse"] = pulse
    newVisit["oxygenLvl"] = oxygenLvl
    if medications != "N/A":
        newVisit["medications"] = medications
        orderMedication = orderMedication
        newVisit["orderMedication"] = orderMedication
    if procedures != "N/A":
        newVisit["procedures"] = procedures
        orderProcedure = orderProcedure
        newVisit["orderProcedure"] = orderProcedure
    if observations != "N/A":
        newVisit["observations"] = observations
    if patientId not in hospital.visits:
        hospital.visits[patientId] = []
    hospital.visits[patientId].append(newVisit)
    print("Visita agregada con éxito")
    print("-" * 20)
    print(newVisit)

def getVisitsById(hospital, patientId):
    visits = []
    for (visitPatientId), visit in hospital.visits.items():
        if visitPatientId == patientId:
            visits.append(visit)
    if not visits:
        raise Exception("El paciente no existe o no tiene registro de visitas")
    return visits

def patientOrders(hospital, patientId):
    orders = []
    for order in hospital.orders:
        if order.patientId == patientId:
            orders.append(order)
    if not orders:
        raise Exception("No se encontraron órdenes para el paciente")
    return orders

def checkOrderById(hospital, orderId):
    for order in hospital.orders:
        if order.id == int(orderId):
            return True
    return False