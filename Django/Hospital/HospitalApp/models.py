from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50)
    cedula = models.BigIntegerField(primary_key=True)
    email = models.CharField(max_length=50)
    phoneNumber = models.IntegerField()
    dateBirth = models.DateField()
    address = models.CharField(max_length=100)
    rol = models.CharField(max_length=50)
    userName = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
        
class Patient(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    dateBirth = models.DateField()
    gender = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    email = models.CharField(max_length=50)

class EmergencyContact(models.Model):
    idUser = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=20)

class Insurance(models.Model):
    idUser = models.ForeignKey(Patient, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    number = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    term = models.CharField(max_length=50)

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    idPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Person, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.CharField(max_length=100)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctorId = models.ForeignKey(Person, on_delete=models.CASCADE)

class Visit(models.Model):
    id = models.AutoField(primary_key=True)
    patientId = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    bloodPressure = models.CharField(max_length=50)
    temperature = models.CharField(max_length=50)
    pulse = models.CharField(max_length=50)
    oxygenLvl = models.CharField(max_length=50)
    orderMedication = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orderMedication")
    orderProcedure = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="orderProcedure")
    observations = models.CharField(max_length=50)

class Medication(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)

class Procedure(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)

class DiagnosticAid(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cost = models.CharField(max_length=50)

class OrderMedication(models.Model):
    id = models.AutoField(primary_key=True)
    idOrder = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder', related_name='orderMedication_Order')
    idMedication = models.ForeignKey(Medication, on_delete=models.CASCADE, default=None)
    dose = models.CharField(max_length=50)
    duration = models.CharField(max_length=50)
    amount = models.CharField(max_length=50)
    item = models.CharField(max_length=50)

class OrderProcedure(models.Model):
    id = models.AutoField(primary_key=True)
    idOrder = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder', related_name='orderProcedure_Order')
    idProcedure = models.ForeignKey(Procedure, on_delete=models.CASCADE, default=None)
    amount = models.CharField(max_length=50)
    frequency = models.CharField(max_length=50)
    item = models.IntegerField()
    specialAssistance = models.BooleanField()
    idSpecialist = models.ForeignKey(Person, on_delete=models.CASCADE, null=True)

class OrderDiagnosticAid(models.Model):
    id = models.AutoField(primary_key=True)
    idOrder = models.ForeignKey(Order, on_delete=models.CASCADE, to_field='id', db_column='idOrder', related_name='orderDiagnositcAid_Order')
    DiagnosticAid = models.ForeignKey(DiagnosticAid, on_delete=models.CASCADE, default=None)
    quantity = models.CharField(max_length=50)
    specialAssistance = models.BooleanField()
    idSpecialist = models.ForeignKey(Person, on_delete=models.CASCADE, null = True)

class Invoice(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateField()
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctorId = models.ForeignKey(Person, on_delete=models.CASCADE)
    medications = models.CharField(max_length=50)
    procedures = models.CharField(max_length=50)
    diagnosticAids = models.CharField(max_length=50)
    totalCost = models.CharField(max_length=50)
    Order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Session(models.Model):
    id = models.AutoField(primary_key=True)
    token = models.CharField(max_length=200)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)