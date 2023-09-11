# serializer.py sirve para convertir los datos nativos que el ORM me provee a un JSON
# y pueda devolverlo como respuesta a travez de esta API
from rest_framework import serializers
from .models import Company, Club

class CompanySerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = '__all__'


class ClubSerializer(serializers.ModelSerializer):

    class Meta:
        model = Club
        fields = '__all__'