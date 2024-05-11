from rest_framework import serializers
from post.models import post, mood_status, place_tag, place
from datetime import datetime, timedelta

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ['id', 'user_id', 'place_id', 'mood_status', 'title', 'content', 'photo', 'mood_tag']

    def get_posts_last_month(self):
        # 한 달 전의 날짜 계산
        last_month_date = datetime.now() - timedelta(days=30)
        # 한 달 이내의 포스트들 가져오기
        posts_last_month = post.objects.filter(created_at__gte=last_month_date)
        # 시리얼화하여 반환
        serializer = self.__class__(posts_last_month, many=True)
        return serializer.data

class placeSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ['id', 'place_name', 'lat', 'lng', 'place_tag', 'photo']