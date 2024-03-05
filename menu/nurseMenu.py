from validators import nurseValidator


def nurseMenu(hospital, idUser):
     while True:
        option=input("1. Registrar Visita\n2. Salir\n")
        if option=="1":
            addVisit(hospital, idUser)
        if option=="2":
            print("Salir")
            return

def addVisit(hospital, idUser):
    try:
        nurseValidator.addVisit(hospital, idUser)
    except Exception as e:
        print(str(e))
