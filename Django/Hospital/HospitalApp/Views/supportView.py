import HospitalApp.validators.supportValidator as supportValidator
from django.http.response import JsonResponse
import json

# ------------------------ MEDICATIONS
def postMedication(self, request):
    try:
        body = json.loads(request.body)
        name = body.get("name")
        cost = body.get("cost")
        supportValidator.createMedication(name, cost)
        message = "Medicamento creado"
        status = 200
    except Exception as e:
        message = str(e)
        status = 400
    response= {"message": message}
    return JsonResponse(response, status=status)

def getMedication(self, request, id = None):
    try:
        medications = [supportValidator.getMedication(id)] if id else supportValidator.getMedications()
        medicationsData = [{"id": medication.id, "name": medication.name, "cost": medication.cost} for medication in medications]
        status = 204 if not medicationsData else 200
    except Exception as e:
        message = str(e)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(medicationsData, safe=False, status=status)

def putMedication(self, request, id = None):
    try:
        body = json.loads(request.body)
        name = body.get("name")
        cost = body.get("cost")
        supportValidator.updateMedication(id, name, cost)
        message = "Medicamento actualizado"
        status = 200
    except Exception as e:
        message = str(e)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)

def deleteMedication(self, request, id = None):
    try:
        supportValidator.deleteMedication(id)
        message = "Medicamento eliminado"
        status = 200
    except Exception as e:
        message = str(e)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)
# ------------------------ MEDICATIONS




# ------------------------ PROCEDURES
def postProcedure(self, request):
    try:
        body = json.loads(request.body)
        name = body.get("name")
        cost = body.get("cost")
        supportValidator.createProcedure(name, cost)
        message = "Procedimiento creado"
        status = 200
    except Exception as e:
        message = str(e)
        status = 400
    response= {"message": message}
    return JsonResponse(response, status=status)

def getProcedure(self, request, id = None):
    try:
        procedures = [supportValidator.getProcedure(id)] if id else supportValidator.getProcedures()
        procedureData = [{"id": procedure.id, "name": procedure.name, "cost": procedure.cost} for procedure in procedures]
        status = 204 if not procedureData else 200
    except Exception as e:
        message = str(e)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(procedureData, safe=False, status=status)

def putProcedure(self, request, id = None):
    try:
        body = json.loads(request.body)
        name = body.get("name")
        cost = body.get("cost")
        supportValidator.updateProcedure(id, name, cost)
        message = "Procedimiento actualizado"
        status = 200
    except Exception as e:
        message = str(e)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)

def deleteProcedure(self, request, id = None):
    try:
        supportValidator.deleteProcedure(id)
        message = "Procedimiento eliminado"
        status = 200
    except Exception as e:
        message = str(e)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)
# ------------------------ PROCEDURES


# ------------------------ DIAGNOSTIC AID
def postDiagnosticAid(self, request):
    try:
        body = json.loads(request.body)
        name = body.get("name")
        cost = body.get("cost")
        supportValidator.createDiagnosticAid(name, cost)
        message = "Ayuda diagnostica creada"
        status = 200
    except Exception as e:
        message = str(e)
        status = 400
    response= {"message": message}
    return JsonResponse(response, status=status)

def getDiagnosticAid(self, request, id = None):
    try:
        diagnosticAids = [supportValidator.getDiagnosticAid(id)] if id else supportValidator.getDiagnosticAids()
        diagnosticAidData = [{"id": diagnosticAid.id, "name": diagnosticAid.name, "cost": diagnosticAid.cost} for diagnosticAid in diagnosticAids]
        status = 204 if not diagnosticAidData else 200
    except Exception as e:
        message = str(e)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(diagnosticAidData, safe=False, status=status)

def putDiagnosticAid(self, request, id = None):
    try:
        body = json.loads(request.body)
        name = body.get("name")
        cost = body.get("cost")
        supportValidator.updateDiagnosticAid(id, name, cost)
        message = "Ayuda diagnostica actualizada"
        status = 200
    except Exception as e:
        message = str(e)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)

def deleteDiagnosticAid(self, request, id = None):
    try:
        supportValidator.deleteDiagnosticAid(id)
        message = "Ayuda diagnostica eliminada"
        status = 200
    except Exception as e:
        message = str(e)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)
# ------------------------ DIAGNOSTIC AID