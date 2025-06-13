from django.db import models


class AD(models.Model):
    nom = models.CharField(max_length=100)
    code_oaci = models.CharField(max_length=4)
    frequence_radio_mhz = models.FloatField()


class Pistes(models.Model):
    id_ad = models.ForeignKey(AD, on_delete=models.CASCADE)
    designation = models.CharField(max_length=7)


class Batiments(models.Model):
    id_ad = models.ForeignKey(AD, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class Aprons(models.Model):
    id_ad = models.ForeignKey(AD, on_delete=models.CASCADE)
    id_batiment = models.ForeignKey(Batiments, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)


class Carburants(models.Model):
    id_ad = models.ForeignKey(AD, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


class Services(models.Model):
    id_ad = models.ForeignKey(AD, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)