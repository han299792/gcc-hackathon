from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from post.models import post, place
from post.serializers import postSerializer, placeSerializer


# Create your views here.
def post_add(request):
    if(request.method == 'POST'):
        data = JSONParser().parse(request)
        serializer = postSerializer(data)
        if(serializer.is_valid):
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error, status = 400)

#사용자 요청시 db에서 위치값을 리턴해줌    
def place_get_in_map(request):
    data = place.objects.all()
    serializer = placeSerializer(data)
    if(serializer.is_valid):
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.error, status = 400)
    
def place_get_in_spot(request):
    data = post.objects.all()
    serializer = postSerializer()
    if(serializer.is_valid):
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.error, status = 400)