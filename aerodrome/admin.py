from django.contrib import admin

from .models import *


class ApronsInline(admin.StackedInline):
    model = Apron
    extra = 1


class ADAdmin(admin.ModelAdmin):
    fields = ["name", "icao_code", "frequency_mhz"]
    inlines = [ApronsInline]


admin.site.register(AD, ADAdmin)