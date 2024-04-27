import HospitalApp.validators.adminValidator as adminValidator
from django.http.response import JsonResponse
import json

def get(self, request, cedula = None):
    try:
        persons = [adminValidator.getUser(cedula)] if cedula else adminValidator.getUsers()
        personsData = [{"name": person.name, "cedula": person.cedula, "email": person.email, "phoneNumber": person.phoneNumber, "dateBirth": person.dateBirth, "address": person.address, "rol": person.rol, "userName": person.userName} for person in persons]
        status = 200 if personsData else 404
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
        return JsonResponse(response, status=status)
    else:
        return JsonResponse(personsData, status=status, safe=False)
            
def post(self, request):
    try:
        body = json.loads(request.body)
        name = body["name"]
        cedula = body["cedula"]
        email = body["email"]
        phoneNumber = body["phoneNumber"]
        dateBirth = body["dateBirth"]
        address = body["address"]
        rol = body["rol"]
        userName = body["userName"]
        password = body["password"]
        adminValidator.createUser(name, cedula, email, phoneNumber, dateBirth, address, rol, userName, password)
        message = "Usuario creado exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status = status) 

def put(self, request, cedula):
    try:
        body = json.loads(request.body)
        adminValidator.updateUser(
            body.get("name"),
            cedula,
            body.get("email"),
            body.get("phoneNumber"),
            body.get("dateBirth"),
            body.get("address"),
            body.get("rol"),
            body.get("userName"),
            body.get("password")
        )
        message = "Usuario actualizado exitosamente"
        status = 200
    except Exception as error:
        message = str(error)
        status = 400
    response = {"message": message}
    return JsonResponse(response, status=status)


def delete(self, request, cedula = None):
    try:
        adminValidator.deleteUser(cedula)
        message = "Usuario eliminado exitosamente"
        status = 204
    except Exception as error:
        message = str(error)
        status = 400
    
    response = {"message": message}
    return JsonResponse(response, status = status)