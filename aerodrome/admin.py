from django.contrib import admin

from .models import *


class ApronsInline(admin.StackedInline):
    model = Aprons
    extra = 1


class ADAdmin(admin.ModelAdmin):
    fields = ["nom", "code_oaci", "frequence_radio_mhz"]
    inlines = [ApronsInline]


admin.site.register(AD, ADAdmin)