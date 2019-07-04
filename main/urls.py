from django.conf.urls import url
from .views import (
    PatientList,
    Login,
    LogoutReq,
    AddItem,
    CartView,
    TestView,
    BillList,
    PatientSelectView,
    FinalBillView,
    GenerateBill,
    AddPatient,
)

urlpatterns = [
    # url(r'patients', PatientListView.as_view(), name='listpatients'),
    url(r'^patientlist/', PatientList, name='listofpatients'),
    url(r'^login/?', Login, name='login'),
    url(r'^logout/?', LogoutReq, name='logout'),
    url(r'^add_item/?', AddItem, name='add_item'),
    url(r'^add_patient/?', AddPatient, name='add_patient'),
    url(r'^cart/?', CartView, name='cartview'),
    url(r'^test/?', TestView, name='testing'),
    url(r'^billhistory/?', BillList, name='listofbills'),
    url(r'^patientselector/?', PatientSelectView, name='patientselect'),
    url(r'^billing/?', FinalBillView, name='finalbill'),
    url(r'^generatebill/?', GenerateBill, name='generateBill'),
]
