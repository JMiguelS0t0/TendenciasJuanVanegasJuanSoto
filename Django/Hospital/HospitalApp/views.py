from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import HospitalApp.Views.adminView as adminView
import HospitalApp.Views.administrativePersonnelView as APView
import HospitalApp.Views.loginView as loginView
import HospitalApp.Views.supportView as supportView
import HospitalApp.Views.doctorView as doctorView

# Create your views here.
class LoginView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        return loginView.post(self, request)

    def get(self, request):
        return loginView.get(self, request)

class PersonView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, cedula = None):
        return adminView.get(self, request, cedula)

    def post(self, request):
        return adminView.post(self, request)

    def put(self, request, cedula = None):
        return adminView.put(self,request, cedula)

    def delete(self, request, cedula = None):
        return adminView.delete(self, request, cedula)

class PatientView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = None):
        return APView.getPatient(self, request, id)

    def post(self, request):
        return APView.postPatient(self, request)

    def put(self, request, id = None):
        return APView.putPatient(self,request, id)

    def delete(self, request, id = None):
        return APView.deletePatient(self, request, id)

class ContactView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = None):
        return APView.getContact(self, request, id)

    def post(self, request):
        return APView.postContact(self, request)

    def put(self, request, id = None):
        return APView.putContact(self,request, id)

    def delete(self, request, id = None):
        return APView.deleteContact(self, request, id)
    

class InsuranceView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = None):
        return APView.getInsurance(self, request, id)

    def post(self, request):
        return APView.postInsurance(self, request)

    def put(self, request, id = None):
        return APView.putInsurance(self,request, id)

    def delete(self, request, id = None):
        return APView.deleteInsurance(self, request, id)

class AppointmentView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = None):
        return APView.getAppointment(self, request, id)

    def post(self, request):
        return APView.postAppointment(self, request)

    def delete(self, request, id = None):
        return APView.deleteAppointment(self, request, id)

class MedicationView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = None):
        return supportView.getMedication(self, request, id)

    def post(self, request):
        return supportView.postMedication(self, request)

    def put(self, request, id = None):
        return supportView.putMedication(self,request, id)

    def delete(self, request, id = None):
        return supportView.deleteMedication(self, request, id)

class ProcedureView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = None):
        return supportView.getProcedure(self, request, id)

    def post(self, request):
        return supportView.postProcedure(self, request)

    def put(self, request, id = None):
        return supportView.putProcedure(self,request, id)

    def delete(self, request, id = None):
        return supportView.deleteProcedure(self, request, id)

class DiagnosticAidView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = None):
        return supportView.getDiagnosticAid(self, request, id)

    def post(self, request):
        return supportView.postDiagnosticAid(self, request)

    def put(self, request, id = None):
        return supportView.putDiagnosticAid(self,request, id)

    def delete(self, request, id = None):
        return supportView.deleteDiagnosticAid(self, request, id)

class MedicalRecordView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = None):
        return doctorView.getMedicalRecords(self, request, id)

    def post(self, request):
        return doctorView.postMedicalRecords(self, request)

class DoctorInfoPatientsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args: any, **kwargs: any):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id = None):
        return doctorView.getBasicInfoPatient(self, request, id)