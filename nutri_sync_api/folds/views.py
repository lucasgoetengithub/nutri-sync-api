from .models import Folds
from .serializers import FoldsSerializer
from rest_framework.response import Response
from rest_framework import generics, status
from django.db.models import Q


class FoldsList(generics.ListCreateAPIView):
    serializer_class = FoldsSerializer

    def get_queryset(self):

        nutri_id = self.request.data.get('nutriID', None)
        patient_id = self.request.data.get('PatientID', None)

        queryset = Folds.objects.all()
        if nutri_id and patient_id:
            filter_expression = Q(nutriId=nutri_id) & Q(patientsId=patient_id)
            queryset = queryset.filter(filter_expression)
        else:
            queryset = queryset.none()

        return queryset

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response({'detail' : 'Dobras criadas/atualizadas com sucesso'}, status=status.HTTP_200_OK)