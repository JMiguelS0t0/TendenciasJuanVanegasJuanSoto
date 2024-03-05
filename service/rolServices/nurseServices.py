import model.models as models
from .administrativePersonnelServices import getPatientById
import datetime

def addVisit(hospital, id, patientId, bloodPressure, temperature, pulse, oxygenLvl, medications, procedures, observations):
    patient = getPatientById(hospital, patientId)
    if patient is None:
        raise Exception("El paciente no existe")
    date = datetime.date.today()
    id =  assignVisitId(hospital.visits)
    newVisit = {}
    newVisit["id"] = id
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
    hospital.visits[(patientId, date)] = newVisit
    print("Visita agregada con exito")
    print("-" * 20)
    print(newVisit)

def updateVisit():
    pass

def deleteVisit():
    pass

def assignVisitId(visits):
    if len(visits) == 0:
        return 1
    else:
        lastId = max(visits.keys(), key=int)
        return int(lastId) + 1