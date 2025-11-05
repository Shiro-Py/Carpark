from django.contrib import admin
from .models import Vehicle

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'license_plate', 'is_active')
    list_filter = ('is_active', 'year')
    search_fields = ('brand', 'model', 'license_plate')