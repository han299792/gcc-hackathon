from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from post.models import post
from post.serializers import postSerializer


# Create your views here.
def post_add(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = postSerializer(data)
        if(serializer.is_valid):
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status = 400)
