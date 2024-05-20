import HospitalApp.models as models
import string, secrets

def login(userName, password):
    try:
        user = models.Person.objects.get(userName=userName)
    except:
        raise Exception("El usuario no existe")
    if user.password != password:
        raise Exception("Contraseña incorrecta")
    activeSession = models.Session.objects.filter(user=user)
    if activeSession.exists():
        raise Exception("Ya hay una sesión activa")
    chars = string.ascii_letters + string.digits
    token = ''.join(secrets.choice(chars) for _ in range(225))
    session = models.Session()
    session.user = user
    session.token = token
    session.save()
    return session

def getSession(token):
    try:
        return models.Session.objects.get(token=token)
    except:
        raise Exception("La sesión no existe")