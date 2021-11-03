from rest_framework import serializers
from core.models import customerModel


class customerSerializer(serializers.ModelSerializer):
    class Meta:
        model=customerModel
        fields="__all__"