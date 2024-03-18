from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', include('patients.urls')),
    path('api/', include('patientsMeasures.urls'))
]
