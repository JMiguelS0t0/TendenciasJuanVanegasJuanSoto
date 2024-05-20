from django.forms import model_to_dict
import HospitalApp.validators.loginValidator as loginValidator
import HospitalApp.service.loginService as loginService
from django.http.response import JsonResponse
import json

def post(self, request):
    try:
        body = json.loads(request.body)
        session = loginValidator.login(body.get("userName"), body.get("password"))
        response = {"message": "Inicio de sesión exitoso", "token": session.token}
        status = 200
    except Exception as error:
        response = {"message": str(error)}
        status = 400
    return JsonResponse(response, status=status)

def get(self, request):
    try:
        token = request.META.get("HTTP_TOKEN")
        session = loginValidator.getSession(token)
        rol = session.user.rol
        status = 200
        response = {"message": "Sesión activa", "rol": rol}
    except Exception as error:
        response = {"message": str(error)}
        status = 400
    return JsonResponse(response, status=status)

def delete(self, request):
    try:
        token = request.META.get("HTTP_TOKEN")
        session = loginValidator.getSession(token)
        session.delete()
        response = {"message": "Sesión cerrada"}
        status = 200
    except Exception as error:
        response = {"message": str(error)}
        status = 400
    return JsonResponse(response, status=status)
    
