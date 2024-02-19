from validators import personTypeValidator
      
def adminMenu(hospital, user):
     while True:
        option=input("1. Crear usuario\n2. Eliminar Usuario\n3. Editar usuario\n4. Salir\n")
        if option=="1":
            createUser(hospital)
        if option=="2":
            break
        if option=="3":
            break
        if option == "4":
            print("Cerrando Sesion")
            return

def createUser(hospital):
    try:
        rol = input("Que rol tendra el usuario?\n")
        personTypeValidator.createUser(hospital, rol) 
        print("Se ha creado el", rol)
    except Exception as error:
        print(str(error))
  