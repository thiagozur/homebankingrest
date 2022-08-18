from rest_framework import serializers
from .models import Cliente

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            'customer_id',
            'customer_name',
            'customer_surname',
            'customer_dni',
            'dob',
            'branch_id',
            'tipo',
        ]