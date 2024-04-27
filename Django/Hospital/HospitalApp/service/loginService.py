import HospitalApp.models as models
import string, secrets

def login(user, password):
    try:
        user = models.Person.objects.get(userName = user)
    except:
        raise Exception("Usuario o contraseña incorrectos")
    if user.password != password:
        raise Exception("Usuario o contraseña incorrectos")
    activeSession = models.Session.objects.filter(user = user)
    if activeSession.exists():
        raise Exception("Ya hay una sesión activa")
    chars = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(chars) for i in range(128))
    session = models.Session()
    session.user = user
    session.token = token
    session.save()
    return session

def getSession(token):
    try:
        return models.Session.objects.get(token = token)
    except:
        raise Exception("El token no existe")
