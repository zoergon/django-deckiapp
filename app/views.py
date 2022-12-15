from rest_framework import viewsets
from .models import Sarja, Pakka
from .serializers import SarjaSerializer, PakkaSerializer

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout

def landingview(request):
    return render(request, 'landingpage.html')

# Loginpage
def loginview(request):
    return render (request, "loginpage.html")


# Login action
def login_action(request):
    user = request.POST['username']
    passw = request.POST['password']
    # Löytyykö kyseistä käyttäjää?
    user = authenticate(username = user, password = passw)
    #Jos löytyy:
    if user:
        # Kirjataan sisään
        login(request, user)
        # Tervehdystä varten context
        context = {'name': user.first_name}
        # Kutsutaan suoraan landingview.html
        return render(request,'landingpage.html',context)
    # Jos ei kyseistä käyttäjää löydy
    else:
        return render(request, 'loginerror.html')


# Logout action
def logout_action(request):
    logout(request)
    return render(request, 'loginpage.html')

def sarjatlistview(request):
    sarjatlist = Sarja.objects.all()
    context = {'sarjat': sarjatlist}
    return render(request, 'sarjatlist.html', context)

def pakatlistview(request):
    pakatlist = Pakka.objects.all()
    sarjatlist = Sarja.objects.all()
    context = {'pakat': pakatlist, 'sarjat': sarjatlist}
    return render(request, 'pakatlist.html', context)

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