from validators import personTypeValidator
      
def adminMenu(hospital, user):
     while True:
        option=input("1. Crear usuario\n2. Eliminar Usuario\n3. Editar usuario\n4. Mostrar Usuarios\n5. Salir\n")
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
        rol = input("Que rol tendra el usuario?\n")
        personTypeValidator.createUser(hospital, rol) 
        print("Se ha creado el", rol)
    except Exception as error:
        print(str(error))

def deleteUser(hospital, cedula):
    try:
        cedula = input("Ingrese la identificación del usuario que desea eliminar: ")
        personTypeValidator.deleteUser(hospital, cedula)
    except Exception as error:
        print(str(error))

def updateUser(hospital, user):
    pass

def getUsers(hospital):
    try:
        personTypeValidator.getAllUsers(hospital)
    except Exception as error:
        print(str(error))