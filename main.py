from model import models
from service import loginService
from menu import adminMenu

hospital = models.Hospital()
admin = models.Person("Admin Admin", "1040570", "admin@admin.com", "297109400", "08/08/2004", "Cra 55b", "admin", "admin", "admin123")
hospital.persons.append(admin)

initialMenu = "1. Iniciar Sesion\n0.Cerrar Programa\n"

def loginRouter(hospital, user):
    if user.rol == "admin":
        print("Bienvenido:", admin.name)
        adminMenu.adminMenu(hospital, user)

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