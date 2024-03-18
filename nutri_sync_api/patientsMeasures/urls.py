from django.urls import path
from .views import PatientsMeasuresList

urlpatterns = [
    path('patientsmeasures/', PatientsMeasuresList.as_view(), name='patients-measure-list'),
]