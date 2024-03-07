from model import models
from service import loginService
from menu import adminMenu, administrativePersonnelMenu, nurseMenu, doctorMenu

hospital = models.Hospital()
user = models.Person("Admin Admin", "1040570", "admin@admin.com", "297109400", "08/08/2004", "Cra 55b", "doctor", "admin", "admin123")
hospital.persons.append(user)
nurse = models.Person("Admin Admin", "1040570", "admin@admin.com", "297109400", "08/08/2004", "Cra 55b", "nurse", "n", "n")
hospital.persons.append(nurse)

patient = models.Patient("1", "John Doe", "01/01/1990", "Male", "123 Main St", "555-1234", "john.doe@example.com")
hospital.clinicalHistory["1"] = {}
emergencyContact = models.EmergencyContact("1", "Jane Doe", "Spouse", "555-5678")
insurance = models.Insurance("1", "ABC Insurance", "123456789", "Active", "01/01/2023")
patient.emergencyContact = emergencyContact
patient.insurance = insurance
hospital.patients.append(patient)
hospital.insurances.append(insurance)
hospital.emergencyContacts.append(emergencyContact)


initialMenu = "1. Iniciar Sesion\n0. Cerrar Programa\n"
def loginRouter(hospital, user):
    if user.rol == "admin":
        print("-- Personal de Recursos Humanos -- ", )
        print("Bienvenid@:")
        adminMenu.adminMenu(hospital, user)
    if user.rol == "Personnel Administrative":
        print("-- Personal Administrativo -- ", )
        print("Bienvenid@:", )
        administrativePersonnelMenu.administrativePersonnelMenu(hospital, user)
    if user.rol == "nurse":
        print("-- Enfermeras -- ", )
        print("Bienvenid@:")
        nurseMenu.nurseMenu(hospital)
    if user.rol == "doctor":
        print("-- Doctores -- ", )
        print("Bienvenid@:")
        doctorMenu.doctorMenu(hospital)

while True:
    option = input(initialMenu)
    print("Ha elegido la opción:", option)
    if option == "1":
        print("Ingrese su usuario:")
        userName = input()
        password = input("Ingrese la contraseña:\n")
        user = loginService.searchUser(hospital, userName)
        if user == None:
            print("Usuario no encontrado")
            continue
        if user.password != password:
            print("Error en usuario o contraseña")
            continue
        loginRouter(hospital, user)
    if option == "0":

        print("Suerte!!")
        break