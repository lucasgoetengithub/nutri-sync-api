from django.shortcuts import render
from .models import Patients
from .serializers import PatientsSerializer
from rest_framework.response import Response
from rest_framework import generics, status

class PatientsList(generics.ListCreateAPIView):
    queryset = Patients.objects.all()
    serializer_class = PatientsSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({'detail': 'Paciente criado com sucesso.'}, status=status.HTTP_201_CREATED)
