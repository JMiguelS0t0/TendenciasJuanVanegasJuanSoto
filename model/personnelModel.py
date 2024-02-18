class Visit():
    def __init__(self, patient, date, bloodPressure, temperature, pulse, oxygenLvl, medicationsAdm, procedures, tests, observations):
        self.patient = patient
        self.date = date
        self.bloodPressure = bloodPressure
        self.temperature = temperature
        self.pulse = pulse
        self.oxygenLvl = oxygenLvl
        self.medicationsAdm = medicationsAdm
        self.procedures = procedures
        self.tests = tests
        self.observations = observations

class MedicalRecord():
    def __init__(self, idPatient, date, idDoctor, reasonConsulta, symptoms, diagnosis):
        self.idPatient = idPatient
        self.date = date
        self.idDoctor = idDoctor
        self.reasonConsulta = reasonConsulta
        self.symptoms = symptoms
        self.diagnosis = diagnosis

class Medications():
    def __init__(self, id, idMedication, dose, duration, item):
        self.id = id
        self.idMedication = idMedication
        self.dose = dose
        self.duration = duration
        self.item = item

class Procedure():
    def __init__(self, id, idProcedure, quantity, frequency, reqAssistance, idSpecialist, item):
        self.id = id
        self.idProcedure = idProcedure
        self.quantity = quantity
        self.frequency = frequency
        self.reqAssistance = reqAssistance
        self.idSpecialist = idSpecialist
        self.item = item

class DiagnosticAid():
    def __init__(self, id, idDiagnosticAid, quantity, reqAssistance, idSpecialist, item):
        self.id = id
        self.idDiagnosticAid = idDiagnosticAid
        self.quantity = quantity
        self.reqAssistance = reqAssistance
        self.idSpecialist = idSpecialist
        self.item = item