from django import views
from django.urls import URLPattern, path

from rest_framework.authtoken import views

from .views import *
from .factories import AddedDetailViewFactory, AddedViewFactory, BaseOfferDetailViewFactory, BaseOfferViewFactory, OrderListDetailViewFactory, OrderListViewFactory


app_name = "api"

urlpatterns = [
    path('base-offer/', APIView_Wrapper.as_view(view_factory=BaseOfferViewFactory)),
    path('base-offer/<int:id>/', DetailAPIView_Wrapper.as_view(view_factory=BaseOfferDetailViewFactory)),
    path('added/', APIView_Wrapper.as_view(view_factory=AddedViewFactory)),
    path('added/<int:id>/', DetailAPIView_Wrapper.as_view(view_factory=AddedDetailViewFactory)),
    path('order-list/', APIView_Wrapper.as_view(view_factory=OrderListViewFactory)),
    path('order-list/<str:id>/', DetailAPIView_Wrapper.as_view(view_factory=OrderListDetailViewFactory)),
    path('token-auth/', views.obtain_auth_token)
]
