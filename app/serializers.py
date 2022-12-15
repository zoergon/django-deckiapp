from rest_framework import serializers
from .models import Sarja, Pakka

class SarjaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sarja
        fields = ['id', 'nimi', 'vuosi']

class PakkaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pakka
        fields = ['id', 'nimi', 'harvinaisuus', 'sarja']