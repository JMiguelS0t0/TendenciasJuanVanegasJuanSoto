from .typeValidator import *
import HospitalApp.service.loginService as loginService

def login(userName, password):
    textValidator(userName, "Username")
    textValidator(password, "Password")
    return loginService.login(userName, password)

def getSession(token):
    textValidator(token, "Token")
    return loginService.getSession(token)