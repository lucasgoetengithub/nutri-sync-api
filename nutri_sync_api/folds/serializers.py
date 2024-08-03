from rest_framework import serializers
from.models import Folds

class FoldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folds
        fields = '__all__'