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
    AppointListView
)

urlpatterns = [
    # url(r'patients', PatientListView.as_view(), name='listpatients'),
    url(r'^patientlist/', PatientList, name='listofpatients'),
    url(r'^login/?', Login, name='login'),
    url(r'^logout/?', LogoutReq, name='logout'),
    url(r'^add_item/?', AddItem, name='add_item'),
    url(r'^add_patient/?', AddPatient, name='add_patient'),
    url(r'^cart/(?P<appointid>[0-9]+)/$', CartView, name='cartview'),
    url(r'^test/?', TestView, name='testing'),
    url(r'^bill/(?P<billid>[0-9]+)/$', FinalBillView, name='finalbill'),
    url(r'^billhistory/?', BillList, name='listofbills'),
    url(r'^appointments/?', AppointListView, name='listofappointments'),
    url(r'^patientselector/?', PatientSelectView, name='patientselect'),
    # url(r'^billing/?', FinalBillView, name='finalbill'),
    url(r'^generatebill/?', GenerateBill, name='generateBill'),
]
