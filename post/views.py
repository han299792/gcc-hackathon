from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from post.models import post, place
from rest_framework.views import APIView
from post.serializers import postSerializer, placeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status


# 캘린더
# -> 최근 한 달 posts 불러오기
# -> 날짜 

# Create your views here.
class posts(APIView):
    
    def get_object(self, pk):
        try:
            return post.objects.get(pk=pk)
        except post.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        serializer = postSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse('post request error', status = 400)
    
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = postSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
