from django.urls import URLPattern, path
from .views import *

app_name = "api"

urlpatterns = [
    path('', index)
]