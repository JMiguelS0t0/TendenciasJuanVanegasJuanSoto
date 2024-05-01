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
        doctorValidator.createMedicalRecord(patientId, idDoctor, consultationReason, symptoms, diagnosis)
        message = "Historia clínica creada exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)

# --------- ORDERS
def getOrdersByPatient(self, request, id=None):
    try:
        orders = doctorValidator.getOrdersByPatient(id)
        if orders.exists():
            orders_data = []
            for order in orders:
                order_data = model_to_dict(order)
                order_data['orderMedications'] = [model_to_dict(medication) for medication in order.orderMedication_Order.all()]
                order_data['orderProcedures'] = [model_to_dict(procedure) for procedure in order.orderProcedure_Order.all()]
                order_data['orderDiagnosticAids'] = [
                    model_to_dict(diagnostic_aid, fields=['id', 'quantity', 'specialAssistance', 'idSpecialist__cedula'])
                    for diagnostic_aid in order.orderDiagnositcAid_Order.all()
                ]
                orders_data.append(order_data)
            status = 200
        else:
            status = 404
            orders_data = []
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(orders_data, status=status, safe=False)

def postOrder(self, request):
    try:
        body = json.loads(request.body)
        patientId = body["patientId"]
        doctorId = body["doctorId"]
        doctorValidator.createOrder(patientId, doctorId)
        message = "Orden creada exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)

def postOrderMedication(self, request):
    try:
        body = json.loads(request.body)
        idOrder = body["idOrder"]
        idMedication = body["idMedication"]
        dose = body["dose"]
        duration = body["duration"]
        amount = body["amount"]
        doctorValidator.createOrderMedication(idOrder, idMedication, dose, duration, amount)
        message = "Orden de medicamento agregada exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)

def postOrderProcedure(self, request):
    try:
        body = json.loads(request.body)
        idOrder = body["idOrder"]
        idProcedure = body["idProcedure"]
        amount = body["amount"]
        frequency = body["frequency"]
        specialAssistance = body["specialAssistance"]
        idSpecialist = body["idSpecialist"]
        doctorValidator.createOrderProcedure(idOrder, idProcedure, amount, frequency, specialAssistance, idSpecialist)
        message = "Orden de procedimiento agregada exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)

def postOrderDiagnosticAid(self, request):
    try:
        body = json.loads(request.body)
        idOrder = body["idOrder"]
        DiagnosticAid = body["DiagnosticAid"]
        quantity = body["quantity"]
        specialAssistance = body["specialAssistance"]
        idSpecialist = body["idSpecialist"]
        doctorValidator.createOrderDiagnosticAid(idOrder, DiagnosticAid, quantity, specialAssistance, idSpecialist)
        message = "Orden de ayuda diagnóstica agregada exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)


# --------- BASIC INFO PATIENTS

def getBasicInfoPatient(self, request, id= None):
    try:
        patient, clinicalHistory = doctorValidator.getBasicInfoPatient(id)
        patientData = model_to_dict(patient)
        patientData["Historias clinicas"] = clinicalHistory
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    return JsonResponse(patientData, status=status)
