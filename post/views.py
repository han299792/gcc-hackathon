from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from post.models import post, place
from rest_framework.views import APIView
from post.serializers import postSerializer, placeSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
import json


# Create your views here.
class posts(APIView):
    
    def get_object(self, pk):
        try:
            return post.objects.get(pk=pk)
        except post.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    @csrf_exempt

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = postSerializer(post)
        return Response(serializer.data)
    
    def post(self, request):
        # try:
        #     data = json.loads(request.body)
        # except json.JSONDecodeError:
        #     return JsonResponse({'detail': 'Invalid JSON format'}, status=400)
        # data = JSONParser().parse(request)
        error = {"error" : "error"}
        serializer = postSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            print('serializer is valid')
            serializer.save()
            return Response(serializer.data, safe=False)
        else:
            print('serializer isn''t valid')
        return Response(error, status = 400)

    
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

def place_get_in_spot(request, pk):
    data = post.objects.filter(posts_id=pk)
    serializer = postSerializer(data)
    if(serializer.is_valid):
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.error, status = 400)

class PostsLastMonthAPIView(APIView):
    def get(self, request, format=None):
        serializer = postSerializer()
        last_month_posts_data = serializer.get_posts_last_month()
        return Response(last_month_posts_data, status=status.HTTP_200_OK)
