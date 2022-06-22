import json
from rest_framework.views import APIView
from django.http import HttpResponse
from django.contrib.auth.models import User

from .poblate import poblate


class BaseOfferAPIView(APIView):
    view_factory = None

    def get(self, request):
        body, status = self.view_factory.create().get()
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')


class AllOffersAPIView(APIView):
    view_factory = None
    queryset = User.objects.none()

    def get(self, request):
        poblate()
        body, status = self.view_factory.create().get()
        return HttpResponse(json.dumps(body), status=status, content_type='application/json')

    def post(self, request):
        try:
            offer = json.loads(request.body)
        except ValueError:
            body = {'error': 'The request body must be in json format.'}
            return HttpResponse(json.dumps(body), status=400, content_type='application/json')
        else:
            body, status = self.view_factory.create().post(offer)
            return HttpResponse(json.dumps(body), status=status, content_type='application/json')
