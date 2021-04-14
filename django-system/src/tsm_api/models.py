from django.db import models


class Measurement(models.Model):
    power = models.DecimalField(max_digits=8, decimal_places=4)
