from validators import nurseValidator

def nurseMenu(hospital):
     while True:
        option=input("1. Registrar Visita\n2. Ver visitas registradas de un paciente\n3. Ver ordenes de paciente\n4. Salir\n")
        if option=="1":
            addVisit(hospital)
        if option=="2":
            getVisitsById(hospital)
        if option=="3":
            patientOrders(hospital)
        if option=="4":
            print("Salir")
            return

def addVisit(hospital):
    try:
        nurseValidator.addVisit(hospital)
    except Exception as e:
        print(str(e))

def getVisitsById(hospital):
    try:
        nurseValidator.getVisitsById(hospital)
    except Exception as e:
        print(str(e))

def patientOrders(hospital):
    try:
        nurseValidator.patientOrders(hospital)
    except Exception as e:
        print(str(e))