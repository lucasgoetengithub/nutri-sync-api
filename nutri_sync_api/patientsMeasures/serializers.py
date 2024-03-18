from rest_framework import serializers
from.models import PatientsMeasures


class PatientsMeasuresSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientsMeasures
        fields = '__all__'