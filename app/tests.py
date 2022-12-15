from django.test import TestCase
from rest_framework.test import APIRequestFactory
from django.urls import reverse
from .views import PakkaViewSet, SarjaViewSet
from .models import Pakka, Sarja


class ViewSetTest(TestCase):
    def test_sarja_view_set(self):
        '''Sarjan lisäys ja haku onnistuu'''
        request = APIRequestFactory().get("")
        sarj_set = SarjaViewSet.as_view({'get': 'retrieve'})

        sarj = Sarja.objects.create(nimi="Jumpstart", vuosi="2020")

        # pk tarkoittaa pääavainta eli id:tä
        response = sarj_set(request, pk=sarj.pk)

        # Testataan että tulee oikea statuskoodi
        self.assertEqual(response.status_code, 200)
        # Testataan että objekti luotiin juuri sellaiseksi kuin oli tarkoitus
        self.assertEqual(response.data, {'id': 1, 'nimi': 'Jumpstart', 'vuosi': "2020"})


    def test_pakka_view_set(self):
            '''Pakan lisäys ja haku onnistuu'''
            request = APIRequestFactory().get("")

            # Deckin lisääminen vaatii tässä ensiksi luotavan opettajan
            sarj_set = SarjaViewSet.as_view({'get': 'retrieve'})
            sarj = Sarja.objects.create(nimi="Jumpstart", vuosi="2020")

            pakka_set = PakkaViewSet.as_view({'get': 'retrieve'})
            pakka = Pakka.objects.create(nimi="Artifacts",
            harvinaisuus=1, sarja_id=sarj.pk)

            response = pakka_set(request, pk=pakka.pk)

            # Testataan että tulee oikea statuskoodi
            self.assertEqual(response.status_code, 200)
            
            # Testataan että objekti luotiin juuri sellaiseksi kuin oli tarkoitus
            self.assertEqual(response.data, {'id': 1, 'nimi': 'Artifacts', 'harvinaisuus': 1, 'sarja': 1})