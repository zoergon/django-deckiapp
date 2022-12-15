from django.db import models

class Sarja(models.Model):
    nimi = models.CharField(max_length=100, default='')
    vuosi = models.CharField(max_length=4, default='')

    class Meta:
        ordering = ['nimi']

class Pakka(models.Model):
    nimi = models.CharField(max_length=100, default='')
    harvinaisuus = models.IntegerField()
    sarja = models.ForeignKey(Sarja, on_delete=models.CASCADE)

    class Meta:
        ordering = ['nimi']