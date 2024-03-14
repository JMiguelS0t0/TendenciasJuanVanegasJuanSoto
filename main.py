from model import models
from service import loginService
from menu import adminMenu, administrativePersonnelMenu, nurseMenu, doctorMenu

hospital = models.Hospital()
# ------- MEDICATION
medication = models.Medication("1", "Paracetamol", "1000")
medication2 = models.Medication("2", "Ibuprofen", "800")
medication3 = models.Medication("3", "Aspirin", "500")
medication4 = models.Medication("4", "Amoxicillin", "250")
medication5 = models.Medication("5", "Lisinopril", "10")
medication6 = models.Medication("6", "Metformin", "1000")
hospital.medications.append(medication)
hospital.medications.append(medication2)
hospital.medications.append(medication3)
hospital.medications.append(medication4)
hospital.medications.append(medication5)
hospital.medications.append(medication6)

# ------- EMPLOYES
user = models.Person("Admin Admin", "1040570", "admin@admin.com", "297109400", "08/08/2004", "Cra 55b", "admin", "admin", "admin123")
hospital.persons.append(user)
nurse = models.Person("Admin Admin", "1040", "admin@admin.com", "297109400", "08/08/2004", "Cra 55b", "nurse", "n", "n")
hospital.persons.append(nurse)
doctor = models.Person("Doctor Name", "1234567", "doctor@example.com", "987654321", "01/01/1980", "123 Main St", "doctor", "d", "d")
hospital.persons.append(doctor)
personnelAdmin = models.Person("Personnel Admin", "9876543", "personnel@admin.com", "123456789", "01/01/1990", "456 Main St", "Personnel Administrative", "pa", "pa")
hospital.persons.append(personnelAdmin)

# ------- PACIENT
patient = models.Patient("1", "John Doe", "01/01/1990", "Male", "123 Main St", "555-1234", "john.doe@example.com")
hospital.clinicalHistory["1"] = {}
emergencyContact = models.EmergencyContact("1", "Jane Doe", "Spouse", "555-5678")
insurance = models.Insurance("1", "ABC Insurance", "123456789", True, "01/01/2023")
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
        doctorMenu.doctorMenu(hospital, user)

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

