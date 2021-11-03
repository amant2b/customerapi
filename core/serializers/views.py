from rest_framework import viewsets
from rest_framework.response import Response
from core.models import customerModel
from .serializers import customerSerializer
import json

class customerApi(viewsets.ModelViewSet):
    queryset=customerModel.objects.all()
    serializer_class= customerSerializer
