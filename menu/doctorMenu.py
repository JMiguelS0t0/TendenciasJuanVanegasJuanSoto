from validators import doctorValidator

def doctorMenu(hospital):
     while True:
        option=input("1. Crear registro medico\n2. Editar registro medico\n3. Salir\n")
        if option=="1":
            addMedicalRecord(hospital)
        if option=="2":
            updateMedicalRecord(hospital)
        if option=="3":
            print("Salir")
            return

def addMedicalRecord(hospital):
    try:
        doctorValidator.addMedicalRecord(hospital)
    except Exception as e:
        print(str(e))

def updateMedicalRecord(hospital):
    pass