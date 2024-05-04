from .typeValidator import *
from HospitalApp.service.rolService import supportService

# ------------------------ MEDICATIONS
# -------------- POST
def createMedication(name, cost):
    name = textValidator(name, "Medicamento")
    cost = textValidator(cost, "Costo")
    supportService.createMedication(name, cost)

# -------------- GET
def getMedications():
    return supportService.getMedications()

def getMedication(id):
    id =  numberValidator(id, "ID")
    return supportService.getMedication(id)

# -------------- DELETE
def deleteMedication(id):
    id =  numberValidator(id, "ID")
    return supportService.deleteMedication(id)

# -------------- UPDATE
def updateMedication(id, name, cost):
    name = textValidator(name, "Medicamento")
    cost = textValidator(cost, "Costo")
    return supportService.updateMedication(id, name, cost)



# ------------------------ PROCEDURES
# -------------- POST
def createProcedure(name, cost):
    name = textValidator(name, "Medicamento")
    cost = textValidator(cost, "Costo")
    supportService.createProcedure(name, cost)

# -------------- GET
def getProcedures():
    return supportService.getProcedures()

def getProcedure(id):
    id =  numberValidator(id, "ID")
    return supportService.getProcedure(id)

# -------------- DELETE
def deleteProcedure(id):
    id =  numberValidator(id, "ID")
    return supportService.deleteProcedure(id)

# -------------- UPDATE
def updateProcedure(id, name, cost):
    name = textValidator(name, "Medicamento")
    cost = textValidator(cost, "Costo")
    return supportService.updateProcedure(id, name, cost)



# ------------------------ DIAGNOSTIC AIDS
# -------------- POST
def createDiagnosticAid(name, cost):
    name = textValidator(name, "Medicamento")
    cost = textValidator(cost, "Costo")
    supportService.createDiagnosticAid(name, cost)

# -------------- GET
def getDiagnosticAids():
    return supportService.getDiagnosticAids()

def getDiagnosticAid(id):
    id =  numberValidator(id, "ID")
    return supportService.getDiagnosticAid(id)

# -------------- DELETE
def deleteDiagnosticAid(id):
    id =  numberValidator(id, "ID")
    return supportService.deleteDiagnosticAid(id)

# -------------- UPDATE
def updateDiagnosticAid(id, name, cost):
    name = textValidator(name, "Medicamento")
    cost = textValidator(cost, "Costo")
    return supportService.updateDiagnosticAid(id, name, cost)