import json
from rest_framework.views import APIView
from django.http import HttpResponse

from .poblate import poblate


class BaseOfferAPIView(APIView):
    view_factory = None

    def get(self, request):
        body, status = self.view_factory.create().get()
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')


class AllOffersAPIView(APIView):
    view_factory = None

    def get(self, request):
        poblate()
        body, status = self.view_factory.create().get()
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def post(self, request, *args, **kwargs):
        body, status = self.view_factory.create().post(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')
