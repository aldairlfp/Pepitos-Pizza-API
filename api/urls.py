from django.urls import URLPattern, path
from .views import *
from .factories import BaseOfferViewFactory

app_name = "api"

urlpatterns = [
    path('base-offer', BaseOfferAPIView.as_view(view_factory=BaseOfferViewFactory))
]