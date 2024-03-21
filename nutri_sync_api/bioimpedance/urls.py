from django.urls import path
from .views import BioimpedanceList

urlpatterns = [
    path('bioimpedance/', BioimpedanceList.as_view(), name='bioimpedance-list')
]