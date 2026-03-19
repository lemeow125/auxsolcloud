"""
Admin configuration for auxsol app
"""

from django.contrib import admin

from .models import Inverter

admin.site.register(Inverter)
