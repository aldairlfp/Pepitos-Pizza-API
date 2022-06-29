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

    def post(self, *args, **kwargs):
        try:
            request_body = json.loads(args[0].body)
        except ValueError:
            body = {'error': 'The request body must be in json format.'}
            return HttpResponse(json.dumps(body), status=400, content_type='application/json', headers={ 'Access-Control-Allow-Origin': '*' })
        else:
            body, status = self.view_factory.create().post(request_body)
            return HttpResponse(json.dumps(body), status=status, content_type='application/json', headers={ 'Access-Control-Allow-Origin': '*' })
    
class DetailAPIView_Wrapper(APIView):
    view_factory = None
    queryset = User.objects.all()
    
    def get(self, request, id):
        body, status = self.view_factory.create().get(id)
        return HttpResponse(json.dumps(body), status=status, content_type='application/json', headers={ 'Access-Control-Allow-Origin': '*' })
    
    def put(self, request, id):
        try:
            request_body = json.loads(request.body)
        except ValueError:
            body = {'error': 'The request body must be in json format.'}
            return HttpResponse(body, status=400, content_type='application/json', headers={ 'Access-Control-Allow-Origin': '*' })
        else:
            body, status = self.view_factory.create().put(request_body, id)
            return HttpResponse(json.dumps(body), status=status, content_type='application/json', headers={ 'Access-Control-Allow-Origin': '*' })
            
    def delete(self, request, id):
        try:
            request_body = json.loads(request.body)
        except ValueError:
            body = {'error': 'The request body must be in json format.'}
            return HttpResponse(body, status=400, content_type='application/json', headers={ 'Access-Control-Allow-Origin': '*' })
        else:
            body, status = self.view_factory.create().delete(id)
            return HttpResponse(json.dumps(body), status=status, content_type='application/json', headers={ 'Access-Control-Allow-Origin': '*' })