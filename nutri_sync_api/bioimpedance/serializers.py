from rest_framework import serializers
from .models import Bioimpedance

class BioimpedanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bioimpedance
        fields = '__all__'