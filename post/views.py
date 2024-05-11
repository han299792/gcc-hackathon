from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.shortcuts import render
from post.models import post, place
from rest_framework.views import APIView
from post.serializers import postSerializer, placeSerializer
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
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
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return JsonResponse({'detail': 'Invalid JSON format'}, status=400)
        data = JSONParser().parse(request)
        serializer = postSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
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
@api_view(['GET'])
def place_get_in_map(request):
    data = place.objects.all()
    serializer = placeSerializer(data)
    if(serializer.is_valid):
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.error, status = 400)
#spot을 눌렀을때 post값을 반환     
@api_view(['GET'])
def place_get_in_spot(request):
    data = post.objects.all()
    serializer = postSerializer()
    if(serializer.is_valid):
        serializer.save()
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.error, status = 400)

class PostsLastMonthAPIView(APIView):
    def get(self, year, month):

        first_day_of_month = datetime(year, month, 1)
        if month == 12:
            first_day_of_next_month = datetime(year + 1, 1, 1)
        else:
            first_day_of_next_month = datetime(year, month + 1, 1)
        last_day_of_month = first_day_of_next_month - timedelta(days=1)

        # 입력받은 월에 생성된 포스트들만 가져오기
        posts_for_month = post.objects.filter(created_at__gte=first_day_of_month,
                                            created_at__lte=last_day_of_month)

        # 시리얼라이즈하여 반환
        serializer = postSerializer(posts_for_month, many=True)
        return Response(serializer.data)

