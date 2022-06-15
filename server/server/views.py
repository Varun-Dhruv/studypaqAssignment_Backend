from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework import status
from rest_framework.response import Response
import requests
import environ
import json

env = environ.Env()
environ.Env.read_env()

@api_view(['GET'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_urls(request):
    res=requests.get(env('URL'))
    urls=[]
    if(res.status_code==200):
        res = res.json()
        data=res['data']['children']
        for x in data:
            urls.append(x['data']['thumbnail'],)
        return JsonResponse({"images": urls}, status=status.HTTP_200_OK)
    if(res.status_code==429):
      
        return JsonResponse({"images":urls,"message": "Error 429:Too many requests please try again later"}, status=status.HTTP_429_TOO_MANY_REQUESTS)
    return(JsonResponse({'hello':'world'}),)
