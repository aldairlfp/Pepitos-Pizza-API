import json
from rest_framework.views import APIView
from django.http import JsonResponse, HttpResponse


class BaseOfferAPIView(APIView):
    view_factory = None

    def get(self, request, *args, **kwargs):
        body, status = self.view_factory.create().get(**kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')


class AllOffersAPIView(APIView):
    view_factory = None

    def get(self, request, *args, **kwargs):
        body, status = self.view_factory.create().get(**kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')
