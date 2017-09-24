from django.contrib import admin

# Register your models here.
from .models import Record


class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount')


admin.site.register(Record, DoctorsAdmin)
