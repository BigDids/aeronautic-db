from django.contrib import admin

from .models import *


@admin.register(AD)
class ADAdmin(admin.ModelAdmin):
    list_display = ["name", "icao_code"]
    search_fields = ["name", "icao_code"]
    autocomplete_fields = ["frequencies"]


@admin.register(RadioFrequency)
class RadioFrequencyAdmin(admin.ModelAdmin):
    search_fields = ["frequency_mhz"]


@admin.register(Runway)
class RunwayAdmin(admin.ModelAdmin):
    list_display = ["designation", "ad"]


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ["name", "building_type", "ad"]


@admin.register(Apron)
class ApronAdmin(admin.ModelAdmin):
    list_display = ["apron_type", "building", "ad"]


@admin.register(Fuel)
class FuelAdmin(admin.ModelAdmin):
    list_display = ["fuel_type", "ad"]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ["service_type", "ad"]
