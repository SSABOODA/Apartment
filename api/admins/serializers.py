from rest_framework import serializers

from api.publics.models import Public

class PublicSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Public
        fields = '__all__'
