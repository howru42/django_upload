from django.db import models


class Record(models.Model):
    name = models.CharField(max_length=256)
    amount = models.FloatField(default=0.0)

    def __str__(self):
        return self.name + " - " + str(self.amount)
