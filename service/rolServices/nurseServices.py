import model.models as models
from .administrativePersonnelServices import getPatientById
import datetime

def addVisit(hospital, patientId, bloodPressure, temperature, pulse, oxygenLvl, medications, procedures, observations):
    patient = getPatientById(hospital, patientId)
    if patient is None:
        raise Exception("El paciente no existe")
    date = datetime.date.today()
    newVisit = {}
    newVisit["patientId"] = patient.id
    newVisit["date"] = date
    newVisit["bloodPressure"] = bloodPressure
    newVisit["temperature"] = temperature
    newVisit["pulse"] = pulse
    newVisit["oxygenLvl"] = oxygenLvl
    if medications != "N/A":
        newVisit["medications"] = medications
    if procedures != "N/A":
        newVisit["procedures"] = procedures
    if observations != "N/A":
        newVisit["observations"] = observations
    if patientId not in hospital.visits:
        hospital.visits[patientId] = []
    hospital.visits[patientId].append(newVisit)
    print("Visita agregada con exito")
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

def deleteVisit():
    pass