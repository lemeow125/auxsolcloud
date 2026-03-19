"""
Common model schemas
"""

from django.db import models


class Inverter(models.Model):
    added_on = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    name = models.CharField(max_length=64, blank=False, null=False)
    auxsol_serial_number = models.CharField(
        max_length=64, blank=False, null=False)
    auxsol_id = models.CharField(max_length=64, blank=False, null=False)
