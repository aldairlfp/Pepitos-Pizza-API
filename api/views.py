import json

from rest_framework.views import APIView, Response
from django.http import HttpResponse
from django.contrib.auth.models import User

from .poblate import Poblation


# class BaseOfferAPIView(APIView):
#     view_factory = None

#     def get(self, request):
#         body, status = self.view_factory.create().get()
#         return Response(body, status=status)


class APIView_Wrapper(APIView):
    view_factory = None
    queryset = User.objects.all()

    def get(self, *args, **kwargs):
        Poblation.poblate()
        body, status = self.view_factory.create().get(*args, **kwargs)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json', headers={ 'Access-Control-Allow-Origin': '*' })

    def post(self, request):
        try:
            request_body = json.loads(request.body)
        except ValueError:
            body = {'error': 'The request body must be in json format.'}
            return Response(body, status=400)
        else:
            body, status = self.view_factory.create().post(request_body)
            return Response(body, status=status)
