from django.db import models


class AD(models.Model):
    name = models.CharField(max_length=100)
    icao_code = models.CharField(max_length=4)
    frequency_mhz = models.FloatField()

    def __str__(self):
        return self.name


class Runway(models.Model):
    ad = models.ForeignKey(AD, on_delete=models.CASCADE, related_name='runways')
    designation = models.CharField(max_length=7)

    def __str__(self):
        return self.designation


class Building(models.Model):
    ad = models.ForeignKey(AD, on_delete=models.CASCADE, related_name='buildings')
    name = models.CharField(max_length=100)
    building_type = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Apron(models.Model):
    ad = models.ForeignKey(AD, on_delete=models.CASCADE, related_name='aprons')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='aprons')
    apron_type = models.CharField(max_length=100)

    def __str__(self):
        return self.apron_type


class FuelType(models.TextChoices):
    MOGAS_98 = "MOGAS_98", "MoGas 98"
    AVGAS_100LL = "AVGAS_100LL", "Avgas 100LL"
    JET_A1 = "JET_A1", "Jet A-1"


class Fuel(models.Model):
    ad = models.ForeignKey(AD, on_delete=models.CASCADE, related_name='fuels')
    fuel_type = models.CharField(max_length=20, choices=FuelType.choices, default=FuelType.JET_A1)

    def __str__(self):
        return self.fuel_type


class ServiceType(models.TextChoices):
    MAINTENANCE_STATION = "MAINTENANCE_STATION", "Maintenance Station"
    AD_INFO = "AD_INFO", "AD Info"
    ATC = "ATC", "ATC"
    NOTAM = "NOTAM", "NOTAM"


class Service(models.Model):
    ad = models.ForeignKey(AD, on_delete=models.CASCADE, related_name='services')
    service_type = models.CharField(max_length=50, choices=ServiceType.choices, default=ServiceType.MAINTENANCE_STATION)

    def __str__(self):
        return self.service_type