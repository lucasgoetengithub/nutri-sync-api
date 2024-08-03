from django.urls import path
from .views import FoldsList

urlpatterns = [
    path('patients/', FoldsList.as_view(), name='patients-list'),
]