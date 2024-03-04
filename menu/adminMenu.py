from validators import adminTypeValidator
      
def adminMenu(hospital, user):
     while True:
        option=input("1. Crear usuario\n2. Eliminar Usuario\n3. Editar usuario\n4.Mostrar Usuarios\n5. Salir\n")
        if option=="1":
            createUser(hospital)
        if option=="2":
            deleteUser(hospital, user)
        if option=="3":
            updateUser(hospital, user)
        if option=="4":
            getUsers(hospital)
        if option == "5":
            print("Cerrando Sesion")
            return

def createUser(hospital):
    try:
        rol = selectRole()
        adminTypeValidator.createUser(hospital, rol) 
        print("Se ha creado el", rol)
    except Exception as error:
        print(str(error))

<<<<<<< HEAD
def deleteUser(hospital, user):
    pass

def updateUser(hospital, user):
    pass
=======

def deleteUser(hospital, cedula):
    try:
        cedula = input("Ingrese la identificación del usuario que desea eliminar: ")
        adminTypeValidator.deleteUser(hospital, cedula)
    except Exception as error:
        print(str(error))

def updateUser(hospital, cedula):
    try:
        cedula = input("Ingrese la identificación del usuario que desea actualizar: ")
        adminTypeValidator.updateUser(hospital, cedula)
    except Exception as error:
        print(str(error))
>>>>>>> c8cb5a0 (ADD - UPDATE PATIENTS (EMERGENCYCONTACT & INSURANCE))

def getUsers(hospital):
    try:
        adminTypeValidator.getAllUsers(hospital)
    except Exception as error:
        print(str(error))


def selectRole():
    print("Seleccione el rol del usuario:")
    print("1. Medico")
    print("2. Personnel Administrative")
    print("3. Admin")
    option = input("Ingrese el número correspondiente al rol: ")
    
    if option == "1":
        rol = "Medico"
    elif option == "2":
        rol = "Personnel Administrative"
    elif option == "3":
        rol = "Admin"
    else:
        raise ValueError("Opción inválida")
    
    return rol