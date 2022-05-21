from django.contrib import admin

from rest_framework.authtoken.admin import TokenAdmin

from .models import *

admin.site.register(BaseOffer)
admin.site.register(Added)
admin.site.register(Amount)
admin.site.register(AmountAdded)
admin.site.register(Offer)

TokenAdmin.raw_id_fields = ['user']

# Register your models here.
