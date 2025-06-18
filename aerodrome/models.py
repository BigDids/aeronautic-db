from django.db import models


class RadioFrequency(models.Model):
    frequency_mhz = models.FloatField(help_text="Frequency in MHz")

    class Meta:
        ordering = ['frequency_mhz']

    def __str__(self):
        return f"{self.frequency_mhz} MHz"


class AD(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the aerodrome")
    icao_code = models.CharField(max_length=4, help_text="ICAO code of the aerodrome")
    frequencies = models.ManyToManyField(
        RadioFrequency,
        help_text="Frequencies used for communication"
    )

    def __str__(self):
        return f"{self.icao_code} - {self.name}"


class Runway(models.Model):
    designation = models.CharField(
        max_length=7,
        help_text="Designation of the runway in format <em>XNN/YNN</em>"
    )
    ad = models.ForeignKey(
        AD,
        on_delete=models.CASCADE,
        related_name='runways',
        help_text="Aerodrome associated with this runway"
    )

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

    name = models.CharField(max_length=100, help_text="Name of the building")
    building_type = models.CharField(
        max_length=50,
        choices=BUILDING_TYPE_CHOICES.items(),
        default=HANGAR,
        help_text="Type of building"
    )
    ad = models.ForeignKey(
        AD,
        on_delete=models.CASCADE,
        related_name='buildings',
        help_text="Aerodrome associated with this building"
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

    name = models.CharField(max_length=50, help_text="Name of the apron")
    apron_type = models.CharField(
        max_length=100,
        choices=APRON_CHOICES.items(),
        default=GENERAL_AVIATION,
        help_text="Type of apron"
    )
    building = models.ForeignKey(
        Building,
        on_delete=models.CASCADE,
        related_name='aprons',
        help_text="Building associated with this apron"
    )
    ad = models.ForeignKey(
        AD,
        on_delete=models.CASCADE,
        related_name='aprons',
        help_text="Aerodrome associated with this apron"
    )

    def __str__(self):
        return f"{self.name} - {self.ad.icao_code}"


class Fuel(models.Model):
    MOGAS_98 = "MOGAS_98"
    AVGAS_100LL = "AVGAS_100LL"
    JET_A1 = "JET_A1"

    FUEL_TYPE_CHOICES = {
        MOGAS_98: "MoGas 98",
        AVGAS_100LL: "Avgas 100LL",
        JET_A1: "Jet A-1",
    }

    fuel_type = models.CharField(
        max_length=20,
        choices=FUEL_TYPE_CHOICES.items(),
        default=MOGAS_98,
        help_text="Type of fuel"
    )
    ad = models.ForeignKey(
        AD,
        on_delete=models.CASCADE,
        related_name='fuels',
        help_text="Aerodrome associated with this fuel"
    )

    def __str__(self):
        label = self.FUEL_TYPE_CHOICES.get(self.fuel_type)
        return f"{label} - {self.ad.icao_code}"


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

    name = models.CharField(max_length=50, help_text="Name of the service")
    service_type = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES.items(),
        default=MAINTENANCE_STATION,
        help_text="Type of service"
    )
    ad = models.ForeignKey(
        AD,
        on_delete=models.CASCADE,
        related_name='services',
        help_text="Aerodrome associated with this service"
    )

    def __str__(self):
        return f"{self.name} - {self.ad.icao_code}"