from django.shortcuts import render
from .models import Patients
from .serializers import PatientsSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from django.db.models import Q

class PatientsList(generics.ListCreateAPIView):
    serializer_class = PatientsSerializer

    def get_queryset(self):
        nutri_id = self.request.query_params.get('nutriID', None)
        name = self.request.query_params.get('name', None)

        queryset = Patients.objects.all()

        if nutri_id:
            queryset = queryset.filter(nutriID=nutri_id)

        if name:
            queryset = queryset.filter(Q(name__icontains=name) | Q(name=''))

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({'detail': 'Paciente criado com sucesso.'}, status=status.HTTP_201_CREATED)


