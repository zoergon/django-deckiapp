from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from . import views

from .views import landingview, sarjatlistview, pakatlistview, loginview, login_action, logout_action

router = routers.DefaultRouter()
router.register(r"sarjat", views.SarjaViewSet, "sarja")
router.register(r"pakat", views.PakkaViewSet, "id")

urlpatterns = [
    path('', landingview),
    # Login & logout
    path('', loginview),
    path('login/', login_action),
    path('logout/', logout_action),
    path('sarjat/', sarjatlistview),
    path('pakat/', pakatlistview),
    # path('admin/', admin.site.urls),
    path("api/", include((router.urls, "app"))),   

]