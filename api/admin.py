from django.contrib import admin

from rest_framework.authtoken.admin import TokenAdmin

from .models import *

TokenAdmin.raw_id_fields = ['user']

# Register your models here.
