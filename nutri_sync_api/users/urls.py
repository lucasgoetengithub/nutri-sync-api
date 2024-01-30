from django.urls import path
from .views import AuthView, UsersList

urlpatterns = [
    path('users/', UsersList.as_view(), name='users-list'),
    path('auth/', AuthView.as_view(), name='auth'),
]