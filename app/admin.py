from django.contrib import admin

# Register your models here.

# jos rekisteröi tälla tavalla adminille oman appin modelit,
# voi myös admin-sivuilta muokata näitä tietoja

from app.models import Sarja, Pakka

@admin.register(Pakka)
class PakkaAdmin(admin.ModelAdmin):
    pass

@admin.register(Sarja)
class SarjaAdmin(admin.ModelAdmin):
    pass
