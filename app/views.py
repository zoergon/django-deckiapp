from rest_framework import viewsets
from .models import Sarja, Pakka
from .serializers import SarjaSerializer, PakkaSerializer

'''Ao. metodi osaa tehdä kaikki crud toiminnot ja hakea opettajat:
    -kaikki opettajat: /api/opettajat
    -opettajan id:llä /api/opettajat/id
    -opettajan nimellä: /api/opettajat/?nimi=joku_nimi
'''

class SarjaViewSet(viewsets.ModelViewSet):
    serializer_class = SarjaSerializer
    def get_queryset(self):
        queryset = Sarja.objects.all()
        nimi = self.request.query_params.get("nimi")
        if nimi is not None:
            queryset = queryset.filter(nimi__icontains=nimi)
        return queryset

'''Ao. metodi osaa tehdä kaikki crud toiminnot ja hakea kurssit:
    -kaikki kurssit: /api/kurssit
    -kurssin id:llä /api/kurssit/id
    -kurssin nimellä: /api/kurssit/?nimi=joku_nimi
    -kurssit opettajan id:llä: /api/kurssit/?opettaja=opettaja_id
'''

class PakkaViewSet(viewsets.ModelViewSet):
    serializer_class = PakkaSerializer
    def get_queryset(self):
        queryset = Pakka.objects.all()
        nimi = self.request.query_params.get("nimi")
        sarja = self.request.query_params.get("sarja")
        if nimi is not None:
            queryset = queryset.filter(nimi=nimi)
        if sarja is not None:
            queryset = queryset.filter(sarja=sarja)
        return queryset