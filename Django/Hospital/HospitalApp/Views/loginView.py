from django.forms import model_to_dict
import HospitalApp.validators.loginValidator as loginValidator
from django.http.response import JsonResponse
import json

def post(self, request):
    try:
        body = json.loads(request.body)
        session = loginValidator.login(body["userName"], body["password"])
        message = "Sesión iniciada exitosamente"
        status = 200
        response = {"message": message, "token": session.token}
    except Exception as error:
        message = str(error)
        status = 400
        response = {"message": message}
    return JsonResponse(response, status = status)

def get(self, request):
    try:
        token = request.META.get('HTTP_TOKEN')
        session = loginValidator.getSession(token)
        rol = session.user.rol
        status = 200
        message = "Token encontrado"
        rol = session.user.rol
    except Exception as error:
        message = str(error)
        status = 400
        rol = None
    response = {"message": message, "rol": rol}
    return JsonResponse(response, status = status)
        
