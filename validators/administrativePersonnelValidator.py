from service.rolServices import administrativePersonnelServices as administrative
from .typeValidator import *

def createPatient(hospital):
    id = numberValidator(input("Ingrese la cedula (ID) del paciente: " + "\n"), "Cedula del paciente")
    name = textValidator(input("Ingrese el nombre del paciente: " + "\n"), "Nombre del paciente")
    dateBirth = dateBirthValidator(input("Ingrese la fecha de nacimiento del paciente: " + "(DD/MM/YYYY)\n"), "Fecha de nacimiento del paciente")
    gender = textValidator(input("Ingrese el genero del paciente: " + "\n"), "Genero del paciente")
    address = addressValidator(input("Ingrese la direccion del paciente: " + "\n"), "La direccion del paciente")
    phoneNumber = phoneNumberValidator(input("Ingrese el numero de telefono del paciente: " + "\n"), "Numero del paciente")
    email = emailValidator(input("Ingrese el correo del paciente:" + "\n"), "Email del paciente")
    administrative.createPacient(hospital, id, name, dateBirth, gender, address, phoneNumber, email)

def getPatient(hospital, id):
    id = str(id)
    patient = administrative.getPatientById(hospital, id)
    if patient:
        print(f"ID: {patient.id}")
        print(f"Nombre: {patient.name}")
        print(f"Fecha de nacimiento: {patient.dateBirth}")
        print(f"Género: {patient.gender}")
        print(f"Dirección: {patient.address}")
        print(f"Número de teléfono: {patient.phoneNumber}")
        print(f"Email: {patient.email}")
    else:
        print("Paciente no encontrado.")
