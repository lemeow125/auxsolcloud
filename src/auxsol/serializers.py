from rest_framework import serializers
from accounts.models import CustomUser
from .models import Inverter


class InverterSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=CustomUser.objects.all(), slug_field='username', required=False)
    added_on = serializers.DateTimeField(format="%I:%M %p", required=False)
    name = serializers.CharField(required=True)
    auxsol_serial_number = serializers.CharField(required=True)
    auxsol_id = serializers.CharField(required=True)

    class Meta:
        model = Inverter
        fields = '__all__'
        read_only_fields = ['user', 'added_on']
