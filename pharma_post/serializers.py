from rest_framework import serializers

from app.models import F_Dose, D_Geographie, D_Type, D_Date


class FDoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = F_Dose
        fields = '__all__'

class DGeographieSerializer(serializers.ModelSerializer):
    class Meta:
        model = D_Geographie
        fields = '__all__'

class DTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = D_Type
        fields = '__all__'

class DDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = D_Date
        fields = '__all__'
