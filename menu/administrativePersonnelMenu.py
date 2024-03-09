from validators import administrativePersonnelValidator

def administrativePersonnelMenu(hospital, user):
    while True:
        option = input("1. Gestionar Pacientes\n2. Programar cita\n3. Generar Factura\n4. Cerrar Sesión\n")
        if option == "1":
            managePatientsMenu(hospital, user)
        if option == "2":
            pass
        if option == "3":
            pass
        if option == "4":
            print("Cerrando Sesion")
            return


def managePatientsMenu(hospital, id):
    while True:
        option = input("1. Registrar Paciente\n2. Editar Paciente\n3. Buscar Paciente\n4. Salir\n")
        if option == "1":
            createPatient(hospital)
        if option == "2":
            updatePatient(hospital, id)
        if option == "3":
            searchPatient(hospital, id)
        if option == "4":
            return

def createPatient(hospital):
    try:
        administrativePersonnelValidator.createPatient(hospital)
        print("Se ha agregado el paciente")
    except Exception as error:
        print(str(error))

def searchPatient(hospital, id):
    try:
        id = input("Ingrese el ID del paciente a buscar: ")
        administrativePersonnelValidator.getPatient(hospital, id)
    except Exception as error:
        print(str(error))

def updatePatient(hospital, id):
    try:
        id = input("Ingrese el ID del paciente a editar: ")
        administrativePersonnelValidator.updatePatient(hospital, id)
    except Exception as error:
        print(str(error))
