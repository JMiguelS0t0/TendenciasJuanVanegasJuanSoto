from HospitalApp import models

def patientInstance(user):
    try:
        patient = models.Patient.objects.get(id = user)
        return patient
    except Exception as e:
        raise Exception("No se encontró ningún paciente con la cédula proporcionada." + str(e))

def personInstance(user):
    try:
        doctor = models.Person.objects.get(cedula = user)
        return doctor
    except Exception as e:
        raise Exception("No se encontró ningún usuario con la cédula proporcionada." + str(e))

def orderInstance(idOrder):
    try:
        order = models.Order.objects.get(id = idOrder)
        return order
    except Exception as e:
        raise Exception("No se encontró ninguna orden con el id proporcionado." + str(e))

def medicationInstance(idMedication):
    try:
        medication = models.Medication.objects.get(id = idMedication)
        return medication
    except Exception as e:
        raise Exception("No se encontró ninguna medicación con el id proporcionado." + str(e))

def procedureInstance(idProcedure):
    try:
        procedure = models.Procedure.objects.get(id = idProcedure)
        return procedure
    except Exception as e:
        raise Exception("No se encontró ningún procedimiento con el id proporcionado." + str(e))

def diagnosticAidInstance(idDiagnosticAid):
    try:
        diagnosticAid = models.DiagnosticAid.objects.get(id = idDiagnosticAid)
        return diagnosticAid
    except Exception as e:
        raise Exception("No se encontró ninguna ayuda diagnóstica con el id proporcionado." + str(e))

def orderMedicationInstance(idOrderMedication):
    try:
        orderMedication = models.OrderMedication.objects.get(id = idOrderMedication)
        return orderMedication
    except Exception as e:
        raise Exception("No se encontró ninguna orden de medicación con el id proporcionado." + str(e))

def itemMedicationInstance(orderId, itemId):
    try:
        itemMedication = models.OrderMedication.objects.get(id= orderId, item=itemId)
        return itemMedication
    except models.OrderMedication.DoesNotExist:
        raise Exception("No se encontró ningún ítem de medicación con el ID proporcionado.")
    except Exception as e:
        raise Exception("Ocurrió un error al obtener el ítem de medicación: " + str(e))

def orderProcedureInstance(idOrderProcedure):
    try:
        orderProcedure = models.OrderProcedure.objects.get(id = idOrderProcedure)
        return orderProcedure
    except Exception as e:
        raise Exception("No se encontró ninguna orden de procedimiento con el id proporcionado." + str(e))

def itemProcedureInstance(orderId, itemId):
    try:
        itemProcedure = models.OrderProcedure.objects.get(id=orderId, item=itemId)
        return itemProcedure
    except models.OrderProcedure.DoesNotExist:
        raise Exception("No se encontró ningún ítem de procedimiento con el ID proporcionado.")
    except Exception as e:
        raise Exception("Ocurrió un error al obtener el ítem de procedimiento: " + str(e))