from django import views
from django.urls import URLPattern, path
from .views import *
from .factories import BaseOfferViewFactory, AllOffersViewFactory

app_name = "api"

urlpatterns = [
    path('base-offer', BaseOfferAPIView.as_view(view_factory=BaseOfferViewFactory)),
    path('offers', AllOffersAPIView.as_view(view_factory=AllOffersViewFactory))
]