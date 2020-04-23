from rest_framework import serializers
from .models import TRGid


class TRGidSerializer(serializers.ModelSerializer):
    class Meta:
        model = TRGid
        fields = '__all__'
