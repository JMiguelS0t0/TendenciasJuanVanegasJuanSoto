from django.forms import model_to_dict
import HospitalApp.validators.doctorValidator as doctorValidator
from django.http.response import JsonResponse
import json

# --------- MEDICAL RECORDS
def getMedicalRecords(self, request, id= None):
    try:
        medicalRecords = [doctorValidator.getMedicalRecords(id)]
        medicalRecordsData = [{
            "id": str((medicalRecord["_id"])),
            "historias": medicalRecord["historias"]
        }for medicalRecord in medicalRecords]
        status = 200 if medicalRecordsData else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(medicalRecordsData, status=status, safe=False)

def postMedicalRecords(self, request):
    try:
        body = json.loads(request.body)
        patientId = body["patientId"]
        idDoctor = body["idDoctor"]
        consultationReason = body["consultationReason"]
        symptoms = body["symptoms"]
        diagnosis = body["diagnosis"]
        order = body["order"]
        doctorValidator.createMedicalRecord(patientId, idDoctor, consultationReason, symptoms, diagnosis, order)
        message = "Historia clínica creada exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)
