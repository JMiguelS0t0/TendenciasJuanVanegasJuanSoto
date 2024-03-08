from validators import doctorValidator
from validators.administrativePersonnelValidator import getPatient

def doctorMenu(hospital, user):
     while True:
        print("\n" + f"Doctor: {user.name}")
        option=input("1. Crear registro medico\n2. Ver datos del paciente\n3. Salir\n")
        if option=="1":
            addMedicalRecord(hospital, user.cedula)
        if option=="2":
            searchPatient(hospital, user)
        if option=="3":
            print("Salir")
            return

def addMedicalRecord(hospital, user):
    try:
        doctorValidator.addMedicalRecord(hospital, user)
    except Exception as e:
        print(str(e))

def searchPatient(hospital, id):
    try:
        id = input("Ingrese el ID del paciente a buscar: ")
        getPatient(hospital, id)
    except Exception as error:
        print(str(error))