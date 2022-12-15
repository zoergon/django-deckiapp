from django.urls import include,path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"sarjat", views.SarjaViewSet, "sarja")
router.register(r"pakat", views.PakkaViewSet, "id")

urlpatterns = [
    path("api/", include((router.urls, "app"))),
]