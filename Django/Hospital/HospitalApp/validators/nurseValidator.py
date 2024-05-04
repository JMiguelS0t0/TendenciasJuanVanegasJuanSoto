from .typeValidator import *
from HospitalApp.service.rolService import nurseService

def createVisit(patientId, bloodPressure, temperature, pulse, oxygenLvl, itemMedication, orderMedication, itemProcedure, orderProcedure, observations):
    patientId = numberValidator(patientId, "id paciente")
    bloodPressure = textValidator(bloodPressure, "presión arterial")
    temperature = textValidator(temperature, "temperatura")
    pulse = textValidator(pulse, "pulso")
    oxygenLvl = textValidator(oxygenLvl, "nivel de oxígeno")
    itemMedication = numberValidator(itemMedication, "id medicamento")
    orderMedication = numberValidator(orderMedication, "id orden")
    itemProcedure = numberValidator(itemProcedure, "id procedimiento")
    orderProcedure = numberValidator(orderProcedure, "id orden")
    observations = textValidatorNone(observations, "observaciones")
    nurseService.addVisit(patientId, bloodPressure, temperature, pulse, oxygenLvl, itemMedication, orderMedication, itemProcedure, orderProcedure, observations)

def getVisitsById(patientId):
    patientId = numberValidator(patientId, "id paciente")
    return nurseService.getVisitsById(patientId)

def patientOrders(patientId):
    patientId = numberValidator(patientId, "id paciente")
    return nurseService.patientOrders(patientId)

def checkOrderById(patientId, orderId):
    patientId = numberValidator(patientId, "id paciente")
    orderId = numberValidator(orderId, "id orden")
    return nurseService.checkOrderById(patientId, orderId)

