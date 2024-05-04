import datetime
from HospitalApp.service.rolService.doctorService import getOrdersByPatient
from HospitalApp import models
from HospitalApp.service import instances

def addVisit(patientId, bloodPressure, temperature, pulse, oxygenLvl, itemMedication, orderMedication, itemProcedure, orderProcedure, observations):
    patient = instances.patientInstance(patientId)
    visitDate = datetime.date.today()

    idItemProcedure = None
    orderId = None
    orderProcedureId = None

    if itemMedication is not None:
        try:
            orderMedicationInstance = models.OrderMedication.objects.select_related('idOrder').get(idOrder=orderMedication, item=itemMedication)
            orderId = orderMedicationInstance.idOrder.id
        except models.OrderMedication.DoesNotExist:
            raise Exception("Ninguna de las órdenes tiene el ítem de medicación solicitado.")
        except Exception as e:
            raise Exception("Error al obtener el ID del item de medicación: " + str(e))

    if itemProcedure is not None and orderProcedure is not None:
        try:
            orderProcedureInstance = models.OrderProcedure.objects.select_related('idOrder').get(idOrder=orderProcedure, item=itemProcedure)
            orderProcedureId = orderProcedureInstance.idOrder.id
            idItemProcedure = itemProcedure
        except models.OrderProcedure.DoesNotExist:
            raise Exception("Ninguna de las órdenes tiene el ítem de procedimiento solicitado.")
        except Exception as e:
            raise Exception("Error al obtener el ID del item de procedimiento: " + str(e))

    visit = models.Visit(patientId=patient, date=visitDate, bloodPressure=bloodPressure, temperature=temperature, pulse=pulse, oxygenLvl=oxygenLvl, itemMedication=itemMedication, orderMedication_id=orderId, itemProcedure=idItemProcedure, orderProcedure_id=orderProcedureId, observations=observations)
    visit.save()

def getVisitsById(patientId):
    try:
        visits = models.Visit.objects.filter(patientId = patientId)
        if visits:
            return visits
        else:
            raise Exception("No se encontraron visitas")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener las visitas. " + str(e))

def patientOrders(patientId):
    order = getOrdersByPatient(patientId)
    return order

def checkOrderById(patientId, orderId):
    try:
        orders = patientOrders(patientId)
        order = orders.filter(id = orderId).first()
        if order:
            return order
        else:
            raise Exception("Order no encontrada")
    except Exception as e:
        raise Exception("Ocurrio un error al obtener la orden" + str(e))