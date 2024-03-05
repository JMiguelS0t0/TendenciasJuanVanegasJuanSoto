from model import models
from service import loginService
from menu import adminMenu, administrativePersonnelMenu

hospital = models.Hospital()
user = models.Person("Admin Admin", "1040570", "admin@admin.com", "297109400", "08/08/2004", "Cra 55b", "Personnel Administrative", "admin", "admin123")
hospital.persons.append(user)

# appointment = models.Appointment("1", "1040570", "1040570", "08/08/2024", "Cita motivo")
# hospital.appointments.append(appointment)

initialMenu = "1. Iniciar Sesion\n0. Cerrar Programa\n"
def loginRouter(hospital, user):
    if user.rol == "admin":
        print("Bienvenido:")
        adminMenu.adminMenu(hospital, user)
    if user.rol == "Personnel Administrative":
        print("Bienvenido:", )
        administrativePersonnelMenu.administrativePersonnelMenu(hospital, user)

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