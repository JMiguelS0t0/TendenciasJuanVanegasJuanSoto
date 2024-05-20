"""
URL configuration for Hospital project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HospitalApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', LoginView.as_view(), name="login"),
# ------------------------ Admin
    path('hospital/person', PersonView.as_view(), name="person post"),
    path('hospital/person/<int:cedula>', PersonView.as_view(), name="person get, put and delete"),
# ------------------------ Admin

# ------------------------ Administrative Personnel
# ------- PATIENT
    path('hospital/patient', PatientView.as_view(), name="patient post"),
    path('hospital/patient/<int:id>', PatientView.as_view(), name="patient get, put and delete"),

# ------- CONTACT
    path('hospital/contact', ContactView.as_view(), name="contact post"),
    path('hospital/contact/<int:id>', ContactView.as_view(), name="contact get, put and delete"),

# ------- INSURANCE
    path('hospital/insurance', InsuranceView.as_view(), name="insurance post"),
    path('hospital/insurance/<int:id>', InsuranceView.as_view(), name="insurance get, put and delete"),

# ------- APPOINTMENT
    path('hospital/appointment', AppointmentView.as_view(), name="appointment post"),
    path('hospital/appointment/<int:id>', AppointmentView.as_view(), name="appointment get and delete"),
# ------------------------ Administrative Personnel

# ------------------------ Information Support
# ------- MEDICATION
    path('hospital/support/medication', MedicationView.as_view(), name="medication post"),
    path('hospital/support/medication/<int:id>', MedicationView.as_view(), name="medication get, put and delete"),

# ------- PROCEDURE
    path('hospital/support/procedure', ProcedureView.as_view(), name="procedure post"),
    path('hospital/support/procedure/<int:id>', ProcedureView.as_view(), name="procedure get, put and delete"),

# ------- DIAGNOSTIC AID
    path('hospital/support/diagnosticaid', DiagnosticAidView.as_view(), name="diagnosticaid post"),
    path('hospital/support/diagnosticaid/<int:id>', DiagnosticAidView.as_view(), name="diagnosticaid get, put and delete"),

# ------------------------ Information Support

# ------------------------ DOCTOR
    path('hospital/doctor/medicalrecord', MedicalRecordView.as_view(), name="medicalrecord post"),
    path('hospital/doctor/medicalrecord/<int:id>', MedicalRecordView.as_view(), name="medicalrecord get"),
    path('hospital/doctor/basicinfopatient/<int:id>', DoctorInfoPatientsView.as_view(), name="basicinfopatient get"),
    path('hospital/doctor/orders/<int:id>', OrdersView.as_view(), name="orders get"),
    path('hospital/doctor/order', OrdersView.as_view(), name="order post"),
    path('hospital/doctor/order/ordermedication', OrderMedicationView.as_view(), name="ordermedication post"),
    path('hospital/doctor/order/orderdiagnosticaid', OrderDiagnosticAidView.as_view(), name="orderdiagnosticaid post"),
    path('hospital/doctor/order/orderprocedure', OrderProcedureView.as_view(), name="orderprocedure post"),
# ------------------------ DOCTOR

# ------------------------ NURSE
    path('hospital/nurse/visit', VisitView.as_view(), name="visit post"),
    path('hospital/nurse/orders/<int:id>', ordersByPatientView.as_view(), name="orders get"),
    path('hospital/nurse/order/<int:idPatient>/<int:idOrder>', orderByPatientAndId.as_view(), name="order get"),
    path('hospital/nurse/visits/<int:id>', VisitView.as_view(), name="visit get"),
# ------------------------ NURSE

]
