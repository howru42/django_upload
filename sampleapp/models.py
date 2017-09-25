from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe


class Record(models.Model):
    name = models.CharField(max_length=256)
    mobile = models.CharField(max_length=11, default=None)
    address = models.CharField(max_length=500, default=None, null=True)
    clinicName = models.CharField(max_length=256, default=None, null=True)
    specialization = models.CharField(max_length=256, default=None, null=True)
    morningTimeSlot = models.TimeField(default=timezone.now, null=True)
    afternoonTimeSlot = models.TimeField(default=timezone.now, null=True)
    eveningTimeSlot = models.TimeField(default=timezone.now, null=True)
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    services = models.CharField(choices=YEAR_IN_SCHOOL_CHOICES, max_length=2, default=FRESHMAN, null=True)

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
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
