from validators import nurseValidator

def nurseMenu(hospital):
     while True:
        option=input("1. Registrar Visita\n2. Ver visitas registradas de un paciente\n3. Salir\n")
        if option=="1":
            addVisit(hospital)
        if option=="2":
            getVisitsById(hospital)
        if option=="3":
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
