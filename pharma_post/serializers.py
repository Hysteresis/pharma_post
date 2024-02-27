from rest_framework import serializers

from app.models import F_Dose


class FDoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = F_Dose
        fields = '__all__'

