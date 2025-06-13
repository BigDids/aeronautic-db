from django.db import models


class AD(models.Model):
    nom = models.CharField(max_length=100)
    code_oaci = models.CharField(max_length=4)
    frequence_radio_mhz = models.FloatField()


class Pistes(models.Model):
    ad = models.ForeignKey(AD, on_delete=models.CASCADE)
    designation = models.CharField(max_length=7)


class Batiments(models.Model):
    ad = models.ForeignKey(AD, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    type = models.CharField(max_length=100)


class Aprons(models.Model):
    ad = models.ForeignKey(AD, on_delete=models.CASCADE)
    batiment = models.ForeignKey(Batiments, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)


class Carburants(models.Model):
    ad = models.ForeignKey(AD, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)


class Services(models.Model):
    ad = models.ForeignKey(AD, on_delete=models.CASCADE)
    type = models.CharField(max_length=100)