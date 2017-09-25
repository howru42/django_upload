from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


class Record(models.Model):
    name = models.CharField(max_length=256)
    mobile = models.CharField(max_length=11, default=None)
    address = models.CharField(max_length=500, default=None, null=True, blank=True)
    clinicName = models.CharField(max_length=256, default=None, null=True)
    morningTimeSlotStart = models.TimeField(null=True, verbose_name='Morning Slot Start Time', blank=True)
    morningTimeSlotEnd = models.TimeField(null=True, verbose_name='Morning Slot End Time', blank=True)
    afternoonTimeSlotStart = models.TimeField(null=True, verbose_name='Afternoon Slot Start Time', blank=True)
    afternoonTimeSlotEnd = models.TimeField(null=True, verbose_name='Afternoon Slot End Time', blank=True)
    eveningTimeSlotStart = models.TimeField(null=True, verbose_name='Evening Slot Start Time', blank=True)
    eveningTimeSlotEnd = models.TimeField(null=True, verbose_name='Evening Slot End Time', blank=True)

    SP_GENERAL_PHYSICAN = '1'
    SP_DENTIST = '2'

    SP_CHOICES = ((SP_DENTIST, 'Dentist'), (SP_GENERAL_PHYSICAN, 'General Physician'),)
    specialization = models.CharField(choices=SP_CHOICES, max_length=1, default=SP_GENERAL_PHYSICAN, null=True)

    SERV_SKIN = '1'
    SERV_HAIR = '2'
    SERV_TATOO = '3'

    SERVICES_CHOICES = ((SERV_SKIN, 'Skin Checks'), (SERV_HAIR, 'Hair Loss Treatment'), (SERV_TATOO, 'Tatoo Removal'))
    services = models.CharField(choices=SERVICES_CHOICES, max_length=1, default=SERV_SKIN, null=True)

    profilePic = models.ImageField(upload_to='profile_pics', verbose_name='Profile Picture', null=True)

    def image_tag(self):
        default_place_holder = 'profile_pics/place_holder.png'
        if self.profilePic.name is None or len(self.profilePic.name) == 0:
            picture = default_place_holder
        else:
            picture = self.profilePic
        return mark_safe('<img src="/%s" width="50" height="50" />' % picture)

    image_tag.short_description = 'Image'

    class Meta(object):
        verbose_name = "Doctor Info"
        verbose_name_plural = "Doctors List"
