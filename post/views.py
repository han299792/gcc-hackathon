from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from post.models import post, place
from rest_framework.views import APIView
from post.serializers import postSerializer, placeSerializer, moodStatusSerializer, placeTagSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta


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
    
    @csrf_exempt
    def post(self, request):
        serializer = postSerializer(data=request.data)
        if(serializer.is_valid(raise_exception=True)):
            serializer.save()
            return Response(serializer.data, safe=False)
        else:
            print('serializer isn''t valid')
        return Response(serializer.errors, status = 400)
    
    @csrf_exempt    
    def delete(self, request, pk, format=None):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @csrf_exempt    
    def put(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = postSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#사용자 요청시 db에서 위치값을 리턴해줌  
@api_view(['GET'])
def place_get_in_map(request):
    data = place.objects.filter(posts.exists)
    serializer = placeSerializer(data)
    if(serializer.is_valid):
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.error, status = 400)

@api_view(['GET'])
def place_get_in_spot(request, pk):
    data = post.objects.filter(posts_id=pk)
    serializer = postSerializer(data)
    if(serializer.is_valid):
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.error, status = 400)

class PostsLastMonthAPIView(APIView):
    def get(self, request, pk):
        # Ensure pk is a string
        year_month = str(pk)  # Use str() for conversion

        # Convert year and month to integers
        print(year_month)
        year, month = int(year_month[:4]), int(year_month[4:])

        # Calculate the first and last day of the month
        first_day_of_month = datetime(year, month, 1)
        if month == 12:
            first_day_of_next_month = datetime(year + 1, 1, 1)
        else:
            first_day_of_next_month = datetime(year, month + 1, 1)
        last_day_of_month = first_day_of_next_month - timedelta(days=1)

        # Fetch posts created within the specified month
        posts_for_month = post.objects.filter(created_date__gte=first_day_of_month,
                                              created_date__lte=last_day_of_month)

        # Serialize the posts and return the response
        serializer = postSerializer(posts_for_month, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def global_place_get(request):
    data = place.objects.all()
    serializer = placeSerializer(data)
    if(serializer.is_valid):
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.error, status = 400)

@api_view(['GET'])
def global_place_get_detail(request, pk):
    data = post.objects.filter(posts_id=pk)
    serializer = postSerializer(data)
    if(serializer.is_valid):
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.error, status = 400)

class MoodStatusView(APIView):
    def post(self, request):
        serializer = moodStatusSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
        return Response(serializer.data)

class PlaceTagView(APIView):
    def post(self, request):
        serializer = placeTagSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
        return Response(serializer.data)