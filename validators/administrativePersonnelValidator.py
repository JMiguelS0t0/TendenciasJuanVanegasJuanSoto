from service.rolServices import administrativePersonnelServices as administrativeS
from .typeValidator import *

# --------------------------------------------------------- PATIENTS
# ------------------------------------------------- CREATES
def createPatient(hospital):
    id = numberValidator(input("Ingrese la cedula (ID) del paciente: " + "\n"), "Cedula del paciente")
    name = textValidator(input("Ingrese el nombre del paciente: " + "\n"), "Nombre del paciente")
    dateBirth = dateBirthValidator(input("Ingrese la fecha de nacimiento del paciente: " + "(DD/MM/YYYY)\n"), "Fecha de nacimiento del paciente")
    try:
        genderInput = input("Ingrese el genero del paciente (1. Masculino - 2. Femenino): ")
        while True:
            if genderInput == "1":
                gender = "masculino"
                break
            elif genderInput == "2":
                gender = "femenino"
                break
            else:
                print("Opción inválida. Por favor, ingrese 1 para masculino o 2 para femenino.")
    except Exception as e:
        print("Ingresa una opción válida.")
    address = addressValidator(input("Ingrese la direccion del paciente: " + "\n"), "La direccion del paciente")
    phoneNumber = phoneNumberValidator(input("Ingrese el numero de telefono del paciente: " + "\n"), "Numero del paciente")
    email = emailValidator(input("Ingrese el correo del paciente:" + "\n"), "Email del paciente")
    administrativeS.createPacient(hospital, id, name, dateBirth, gender, address, phoneNumber, email)
    print("-" * 20)
    createEmergencyContact(hospital, id)
    print("-" * 20)
    createInsurance(hospital, id)
    
def createEmergencyContact(hospital, idUser):
    name = textValidator(input("Ingrese el nombre del contacto de emergencia del paciente: " + "\n"), "Nombre del contacto de emergencia del paciente")
    relationship = textValidator(input("Ingrese la relacion del contacto de emergencia con el paciente: " + "\n"), "Relacion del contacto de emergencia con el paciente")
    phoneNumber = phoneNumberValidator(input("Ingrese el numero de telefono del contacto de emergencia del paciente: " + "\n"), "Numero del contacto de emergencia del paciente")
    administrativeS.createEmergencyContact(hospital, idUser, name, relationship, phoneNumber)

def createInsurance(hospital, idUser):
    company = textValidator(input("Ingrese el nombre del seguro medico: " + "\n"), "Nombre del seguro medico")
    number = numberValidator(input("Ingrese el numero de póliza del seguro medico : " + "\n"), "Numero de poliza del seguro medico")
    status = getInsuranceStatus()
    term = futureDateValidator(input("Ingrese la fecha de finalizacion del seguro medico: " + "(DD/MM/YYYY)\n"), "Fecha de finalizacion del seguro medico")
    administrativeS.createInsurance(hospital, idUser, company, number, status, term)
# ------------------------------------------------- CREATES

# ------------------------------------------------- UPDATES
def updatePatient(hospital, id):
    nameInput = input("Ingrese el nuevo nombre del paciente: " + "\n") or "No update"
    name = textValidator(nameInput, "Nombre del paciente")
    
    dateBirth = None
    dateBirthInput = input("Ingrese la nueva fecha de nacimiento del paciente: " + "(DD/MM/YYYY)\n") or "No Update"
    if dateBirthInput != "No Update":
        dateBirth = dateBirthValidator(dateBirthInput, "Fecha de nacimiento del paciente")
    
    try:
        genderInput = input("Ingrese el genero del paciente (1. Masculino - 2. Femenino): ")
        while True:
            if genderInput == "1":
                gender = "masculino"
                break
            elif genderInput == "2":
                gender = "femenino"
                break
            elif genderInput == "":
                gender = "No update"
                break
            else:
                print("Opción inválida. Por favor, ingrese 1 para masculino o 2 para femenino.")
    except Exception as e:
        print("Ingresa una opción válida.")
    
    addressInput = input("Ingrese la nueva direccion del paciente: " + "\n") or "No update"
    address = addressValidator(addressInput, "La direccion del paciente")
    
    phoneNumber = None
    phoneNumberInput = input("Ingrese el nuevo numero de telefono del paciente: " + "\n") or "No Update"
    if phoneNumberInput != "No Update":
        phoneNumber = phoneNumberValidator(phoneNumberInput, "Numero del paciente")
    
    email = None
    emailInput = input("Ingrese el nuevo correo del paciente:" + "\n") or "No Update"
    if emailInput != "No Update":
        email = emailValidator(emailInput, "Email del paciente")
    
    administrativeS.updatePacient(hospital, id, name, dateBirth, gender, address, phoneNumber, email)

    while True:
        try:
            print("¿Deseas actualizar la información del contacto de emergencia? (Sí/No)")
            answer = input().lower()
            if answer == "si":
                updateEmergencyContact(hospital, id)
                break
            elif answer == "no":
                break
            else:
                print("Por favor, ingresa una opción válida (Sí/No).")
        except Exception as e:
            print("Ingresa una opción válida.")

    while True:
        try:
            print("¿Deseas actualizar la información del seguro médico? (Sí/No)")
            answer = input().lower()
            if answer == "si":
                updateInsurance(hospital, id)
                break
            elif answer == "no":
                break
            else:
                print("Por favor, ingresa una opción válida (Sí/No).")
        except Exception as e:
            print("Ingresa una opción válida.")

    print("Datos del paciente actualizados correctamente.")
    
def updateEmergencyContact(hospital, idUser):
    nameInput = input("Ingrese el nuevo nombre del contacto de emergencia del paciente: " + "\n") or "No update"
    name = textValidator(nameInput, "Nombre del contacto de emergencia del paciente")
    
    relationshipInput = input("Ingrese la nueva relacion del contacto de emergencia con el paciente: " + "\n") or "No update"
    relationship = textValidator(relationshipInput, "Relacion del contacto de emergencia con el paciente")
    
    phoneNumberInput = input("Ingrese el nuevo numero de telefono del contacto de emergencia del paciente: " + "\n") or "No update"
    if phoneNumberInput != "No update":
        phoneNumber = phoneNumberValidator(phoneNumberInput, "Numero del contacto de emergencia del paciente")
    else:
        phoneNumber = "No update"
    administrativeS.updateEmergencyContact(hospital, idUser, name, relationship, phoneNumber)

def updateInsurance(hospital, idUser):
    companyInput = input("Ingrese el nuevo nombre del seguro medico: " + "\n") or "No update"
    company = textValidator(companyInput, "Nombre del seguro medico")
    
    numberInput = input("Ingrese el nuevo numero de póliza del seguro medico : " + "\n") or "No update"
    if numberInput != "No update":
        number = numberValidator(numberInput, "Numero de poliza del seguro medico")
    else:
        number = "No update"

    status = getInsuranceStatus()
    
    termInput = input("Ingrese la nueva fecha de finalizacion del seguro medico: " + "\n") or "No update"
    if termInput != "No update":
        term = futureDateValidator(termInput, "Fecha de finalizacion del seguro medico")
    else:
        term = "No update"

    administrativeS.updateInsurance(hospital, idUser, company, number, status, term)
# ------------------------------------------------- UPDATES

# ------------------------------------------------- GET
def getPatient(hospital, id):
    id = str(id)
    patient = administrativeS.getPatientById(hospital, id)
    if patient:
        print(f"ID: {patient.id}")
        print(f"Nombre: {patient.name}")
        print(f"Fecha de nacimiento: {patient.dateBirth}")
        print(f"Género: {patient.gender}")
        print(f"Dirección: {patient.address}")
        print(f"Número de teléfono: {patient.phoneNumber}")
        print(f"Email: {patient.email}")
        if patient.emergencyContact:
            print("-" * 20)
            print("Contacto de Emergencia:")
            print(f"Nombre: {patient.emergencyContact.name}")
            print(f"Relación: {patient.emergencyContact.relationship}")
            print(f"Número de teléfono: {patient.emergencyContact.phoneNumber}")
        if patient.insurance:
            print("-" * 20)
            print("Informacion de Poliza:")
            print(f"Compañia: {patient.insurance.company}")
            print(f"Numero de poliza: {patient.insurance.number}")
            print(f"Estado de poliza: {patient.insurance.status}")
            print(f"Estado de poliza: {patient.insurance.term}")
    else:
        print("Paciente no encontrado.")
# ------------------------------------------------- GET
# ------------------------------------------------------- PATIENTS

# -------------------------------------------------------- APPOINTMENTS
def scheduleAppointment(hospital):
    id = administrativeS.assignAppointmentId(hospital)
    idUser = numberValidator(input("Ingrese la cedula (ID) del paciente: " + "\n"), "Cedula del paciente")
    doctorName = textValidator(input("Ingrese el nombre del doctor: " + "\n"), "Nombre del doctor")
    date = futureDateValidator(input("Ingrese la fecha de la cita: " + "(DD/MM/YYYY)\n"), "Fecha de la cita")
    reason = textValidator(input("Ingrese el motivo de la cita: " + "\n"), "Motivo de la cita")
    
    patient = administrativeS.getPatientById(hospital, str(idUser))
    if not patient:
        print("El paciente no existe.")
        print("¿Desea agregar al paciente? (Sí/No)")
        answer = input().lower()
        if answer == "si":
            createPatient(hospital)
        else:
            print("La cita no se puede programar sin un paciente existente.")
            return
    administrativeS.scheduleAppointment(hospital, str(id), str(idUser), doctorName, date, reason)

def patientAppointmentHistory(hospital, idUser):
    appointments = administrativeS.getAppointmentsByUserId(hospital, str(idUser))
    if appointments:
        print(f"Citas del paciente con ID {idUser}:")
        for appointment in appointments:
            print(f"Id: {appointment.id}")
            print(f"Fecha: {appointment.date}")
            print(f"Doctor: {appointment.doctorName}")
            print(f"Motivo: {appointment.reason}")
            print("-" * 20)
    else:
        print("No se encontraron citas para el paciente con ID {idUser}.")

# -------------------------------------------------------- APPOINTMENTS

# -------------------------------------------------------- OTHERS
def getInsuranceStatus():
    while True:
        status_input = input("¿El seguro está activo? (Si/No): ").lower()
        if status_input == "si" or status_input == "si":
            return True
        elif status_input == "no":
            return False
        else:
            print("Por favor, responda 'Sí' o 'No'.")