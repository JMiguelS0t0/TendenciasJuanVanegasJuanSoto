from django.forms import model_to_dict
import HospitalApp.validators.nurseValidator as nurseValidator
from django.http.response import JsonResponse
import json

def addVisit(self, request):
    try:
        body = json.loads(request.body)
        patientId = body["patientId"]
        bloodPressure = body["bloodPressure"]
        temperature = body["temperature"]
        pulse = body["pulse"]
        oxygenLvl = body["oxygenLvl"]
        itemMedication = body["itemMedication"]
        orderMedication = body["orderMedication"]
        itemProcedure = body["itemProcedure"]
        orderProcedure = body["orderProcedure"]
        observations = body["observations"]
        nurseValidator.createVisit(patientId, bloodPressure, temperature, pulse, oxygenLvl, itemMedication, orderMedication, itemProcedure, orderProcedure, observations)
        message = "Visita agregada correctamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)

def getVisitsById(self, request, id=None):
    try:
        visits = nurseValidator.getVisitsById(id)
        if visits.exists():
            visitsData = [{
                "id": visit.id,
                "patientId": visit.patientId.id,
                "date": visit.date,
                "bloodPressure": visit.bloodPressure,
                "temperature": visit.temperature,
                "pulse": visit.pulse,
                "oxygenLvl": visit.oxygenLvl,
                "Medicamentos": {} if visit.itemMedication is None and visit.orderMedication is None else {
                    "item Medication": visit.itemMedication,
                    "order of Medication": visit.orderMedication.id if visit.orderMedication else None
                },
                "Procedimientos": {} if visit.itemProcedure is None and visit.orderProcedure is None else {
                    "item Procedure": visit.itemProcedure,
                    "order of Procedure": visit.orderProcedure.id if visit.orderProcedure else None
                },
                "observations": visit.observations
            } for visit in visits]
            status = 200
        else:
            status = 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(visitsData, status=status, safe=False)

def getOrdersByPatient(self, request, id=None):
    try:
        orders = nurseValidator.patientOrders(id)
        if orders.exists():
            ordersData = []
            for order in orders:
                orderData = getOrderData(order)
                ordersData.append(orderData)
            status = 200
        else:
            status = 404
            ordersData = []
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(ordersData, status=status, safe=False)

def checkOrderById(self, request, idPatient = None, idOrder = None):
    try:
        order = nurseValidator.checkOrderById(idPatient, idOrder)
        if order:
            orderData = getOrderData(order)
            status = 200
        else:
            status = 404
            orderData = []
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(orderData, status=status, safe=False)


# --------- OTHERS
def getOrderData(order):
    orderData = model_to_dict(order)
    orderData['orderMedications'] = getOrderMedications(order)
    orderData['orderProcedures'] = getOrderProcedures(order)
    orderData['orderDiagnosticAids'] = getOrderDiagnosticAids(order)
    return orderData

def getOrderMedications(order):
    return [model_to_dict(medication) for medication in order.orderMedication_Order.all()]

def getOrderProcedures(order):
    return [model_to_dict(procedure) for procedure in order.orderProcedure_Order.all()]

def getOrderDiagnosticAids(order):
    return [
        model_to_dict(diagnostic_aid, fields=['id', 'quantity', 'specialAssistance', 'idSpecialist__cedula'])
        for diagnostic_aid in order.orderDiagnositcAid_Order.all()
    ]