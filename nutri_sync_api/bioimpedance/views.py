from django.shortcuts import render
from .models import Bioimpedance
from .serializers import BioimpedanceSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from django.db.models import Q

class BioimpedanceList(generics.ListCreateAPIView):
    serializer_class = BioimpedanceSerializer

    def get_queryset(self):

        nutri_id = self.request.data.get('nutriID', None)
        patient_id = self.request.data.get('PatientID', None)

        queryset = Bioimpedance.objects.all()
        if nutri_id and patient_id:
            filter_expression = Q(nutriId=nutri_id) & Q(patientId=patient_id)
            queryset = queryset.filter(filter_expression)
        else:
            queryset = queryset.none()

        return queryset
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({'detail' : 'Bioimpedancia criada/atualizada com sucesso'}, status=status.HTTP_200_OK)
