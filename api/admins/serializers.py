from api.publics.models import Public
from rest_framework import serializers

from .models import Admin
from api.publics.serializers import PublicSerializer 

class AdminSerializer(serializers.ModelSerializer):
    public = PublicSerializer(source='public_set', many=True)
    
    class Meta:
        model = Admin
        fields = '__all__'

