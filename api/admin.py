from django.contrib import admin

from rest_framework.authtoken.admin import TokenAdmin

from .models import *

admin.site.register(BaseOffer)
admin.site.register(Added)
admin.site.register(RequestedOffer)
admin.site.register(Client)
admin.site.register(Order)
admin.site.register(OrderList)

TokenAdmin.raw_id_fields = ['user']

# Register your models here.
