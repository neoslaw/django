from django.contrib import admin
from .models import Rental

class RentalAdmin(admin.ModelAdmin):
    search_fields = ['who','what','when','returned']
    ordering = ['who','what','when','returned']


admin.site.register(Rental, RentalAdmin)
