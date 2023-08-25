from rest_framework import serializers
from .models import PC


class PCSerializer(serializers.ModelSerializer):
    class Meta:
        model = PC
        fields = "__all__"
