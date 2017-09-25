from django.contrib import admin

# Register your models here.
from django.utils.safestring import mark_safe

from .models import Record

# admin.site.site_header = 'My administration'


class DoctorsAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'mobile', 'clinicName', 'services')
    fields = ('name', 'mobile', 'profilePic', 'services', 'morningTimeSlot')
    readonly_fields = ('image_tag',)

    def display_name(self, record):
        default_place_holder = 'profile_pics/place_holder.png'
        if len(record.profilePic.name) == 0:
            picture = default_place_holder
        else:
            picture = record.profilePic
        return mark_safe(
            '<p><img src="/%s" width="50" height="50" style="margin-right:30px" />%s</p>' % (picture, record.name))

    display_name.short_description = 'Profile'


admin.site.register(Record, DoctorsAdmin)
