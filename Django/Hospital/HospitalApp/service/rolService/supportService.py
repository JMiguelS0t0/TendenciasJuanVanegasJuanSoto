from HospitalApp import models 

# ------------------------ MEDICATIONS
# -------------- POST

def createMedication(name, cost):
    medication = models.Medication(name=name, cost=cost)
    medication.save()

# -------------- GET
def getMedications():
    try:
        medications = models.Medication.objects.all()
        if medications:
            return medications
        else:
            raise Exception("No se encontraron medicamentos")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener los medicamentos. " + str(e))

def getMedication(id):
    try:
        medication = models.Medication.objects.filter(id=id).first()
        if medication:
            return medication
        else:
            raise Exception("No se encontró el medicamento")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener el medicamento. " + str(e))

# -------------- UPDATE
def updateMedication(id, name, cost):
    try:
        medication = models.Medication.objects.filter(id=id).first()
        if medication:
            medication.name = name
            medication.cost = cost
            medication.save()
            return medication
        else:
            raise Exception("No se encontró el medicamento")
    except Exception as e:
        raise Exception("Ocurrio un error al actualizar el medicamento. " + str(e))

# -------------- DELETE
def deleteMedication(id):
    try:
        medication = models.Medication.objects.filter(id=id).first()
        if medication:
            medication.delete()
        else:
            raise Exception("No se encontró el medicamento")
    except Exception as e:
        raise Exception("Ocurrio un error al eliminar el medicamento. " + str(e))




# ------------------------ PROCEDURES
# -------------- POST

def createProcedure(name, cost):
    procedure = models.Procedure(name=name, cost=cost)
    procedure.save()

# -------------- GET
def getProcedures():
    try:
        procedures = models.Procedure.objects.all()
        if procedures:
            return procedures
        else:
            raise Exception("No se encontraron procedimientos")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener los procedimientos. " + str(e))

def getProcedure(id):
    try:
        procedure = models.Procedure.objects.filter(id=id).first()
        if procedure:
            return procedure
        else:
            raise Exception("No se encontró el procedimiento")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener el procedimiento. " + str(e))

# -------------- UPDATE
def updateProcedure(id, name, cost):
    try:
        procedure = models.Procedure.objects.filter(id=id).first()
        if procedure:
            procedure.name = name
            procedure.cost = cost
            procedure.save()
        else:
            raise Exception("No se encontró el procedimiento")
    except Exception as e:
        raise Exception("Ocurrio un error al actualizar el procedimiento. " + str(e))

# -------------- DELETE
def deleteProcedure(id):
    try:
        procedure = models.Procedure.objects.filter(id=id).first()
        if procedure:
            procedure.delete()
        else:
            raise Exception("No se encontró el procedimiento")
    except Exception as e:
        raise Exception("Ocurrio un error al eliminar el procedimiento. " + str(e))




# ------------------------ DIAGNOSTIC AIDS
# -------------- POST

def createDiagnosticAid(name, cost):
    diagnosticAid = models.DiagnosticAid(name=name, cost=cost)
    diagnosticAid.save()

# -------------- GET
def getDiagnosticAids():
    try:
        diagnosticAids = models.DiagnosticAid.objects.all()
        if diagnosticAids:
            return diagnosticAids
        else:
            raise Exception("No se encontraron ayudas diagnosticas")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener las ayudas diagnosticas. " + str(e))

def getDiagnosticAid(id):
    try:
        diagnosticAid = models.DiagnosticAid.objects.filter(id=id).first()
        if diagnosticAid:
            return diagnosticAid
        else:
            raise Exception("No se encontró la ayuda diagnostica")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener la ayuda diagnostica. " + str(e))

# -------------- UPDATE
def updateDiagnosticAid(id, name, cost):
    try:
        diagnosticAid = models.DiagnosticAid.objects.filter(id=id).first()
        if diagnosticAid:
            diagnosticAid.name = name
            diagnosticAid.cost = cost
            diagnosticAid.save()
        else:
            raise Exception("No se encontró la ayuda diagnostica")
    except Exception as e:
        raise Exception("Ocurrio un error al actualizar la ayuda diagnostica. " + str(e))

# -------------- DELETE
def deleteDiagnosticAid(id):
    try:
        diagnosticAid = models.DiagnosticAid.objects.filter(id=id).first()
        if diagnosticAid:
            diagnosticAid.delete()
        else:
            raise Exception("No se encontró la ayuda diagnostica")
    except Exception as e:
        raise Exception("Ocurrio un error al eliminar la ayuda diagnostica. " + str(e))