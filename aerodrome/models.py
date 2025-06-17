from django.db import models


class RadioFrequency(models.Model):
    frequency_mhz = models.FloatField()

    class Meta:
        ordering = ['frequency_mhz']

    def __str__(self):
        return f"{self.frequency_mhz} MHz"


class AD(models.Model):
    name = models.CharField(max_length=100)
    icao_code = models.CharField(max_length=4)
    frequencies = models.ManyToManyField(RadioFrequency)

    def __str__(self):
        return f"{self.icao_code} - {self.name}"


class Runway(models.Model):
    ad = models.ForeignKey(AD, on_delete=models.CASCADE, related_name='runways')
    designation = models.CharField(max_length=7)

    def __str__(self):
        return f"{self.designation} - {self.ad.icao_code}"


class Building(models.Model):
    HANGAR = "HANGAR"
    MAINTENANCE = "MAINTENANCE"
    CONTROL_TOWER = "CONTROL_TOWER"
    SECURITY_OFFICE = "SECURITY_OFFICE"
    GAS_STATION = "GAS_STATION"

    BUILDING_TYPE_CHOICES = {
        HANGAR: "Hangar",
        MAINTENANCE: "Maintenance",
        CONTROL_TOWER: "Control Tower",
        SECURITY_OFFICE: "Security Office",
        GAS_STATION: "Gas Station",
    }

    ad = models.ForeignKey(AD, on_delete=models.CASCADE, related_name='buildings')
    name = models.CharField(max_length=100)
    building_type = models.CharField(
        max_length=50,
        choices=BUILDING_TYPE_CHOICES.items(),
        default=HANGAR,
    )

    def __str__(self):
        return f"{self.name} - {self.ad.icao_code}"


class Apron(models.Model):
    GENERAL_AVIATION = "GENERAL_AVIATION"
    TRAINING = "TRAINING"
    HELICOPTER = "HELICOPTER"
    MAINTENANCE = "MAINTENANCE"

    APRON_CHOICES = {
        GENERAL_AVIATION: "General Aviation Apron",
        TRAINING: "Training Apron",
        HELICOPTER: "Helicopter Apron",
        MAINTENANCE: "Maintenance Apron",
    }

    ad = models.ForeignKey(AD, on_delete=models.CASCADE, related_name='aprons')
    building = models.ForeignKey(Building, on_delete=models.CASCADE, related_name='aprons')
    apron_type = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.apron_type} - {self.building} - {self.ad.icao_code}"


class Fuel(models.Model):
    MOGAS_98 = "MOGAS_98"
    AVGAS_100LL = "AVGAS_100LL"
    JET_A1 = "JET_A1"

    FUEL_TYPE_CHOICES = {
        MOGAS_98: "MoGas 98",
        AVGAS_100LL: "Avgas 100LL",
        JET_A1: "Jet A-1",
    }

    ad = models.ForeignKey(AD, on_delete=models.CASCADE, related_name='fuels')
    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_TYPE_CHOICES.items(),
        default=MOGAS_98
    )

    def __str__(self):
        return f"{self.fuel_type} - {self.ad.icao_code}"


class Service(models.Model):
    MAINTENANCE_STATION = "MAINTENANCE_STATION"
    AD_INFO = "AD_INFO"
    ATC = "ATC"
    NOTAM = "NOTAM"

    SERVICE_CHOICES = {
        MAINTENANCE_STATION: "Maintenance Station",
        AD_INFO: "AD Info",
        ATC: "ATC",
        NOTAM: "NOTAM",
    }

    ad = models.ForeignKey(AD, on_delete=models.CASCADE, related_name='services')
    service_type = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES.items(),
        default=MAINTENANCE_STATION
    )

    def __str__(self):
        return f"{self.service_type} - {self.ad.icao_code}"