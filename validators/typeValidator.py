def textValidator(string,element):
    if string==None or string=="":
        raise Exception(element + "no es un valor es valido")

def numberValidator(string,element):
    textValidator(string,element)
    try:
        return int(string)
    except:
        raise Exception(element + " no es un numero valido")