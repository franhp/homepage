from django.contrib.gis import admin
from places.models import City, Country, Visit


class CustomVisit(admin.ModelAdmin):
    list_display = ("date", "attendants", "city", "display")


admin.site.register(City, admin.OSMGeoAdmin)
admin.site.register(Country)
admin.site.register(Visit, CustomVisit)
