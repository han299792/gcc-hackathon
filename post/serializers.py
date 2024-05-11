from rest_framework import serializers
from post.models import post, mood_status, place_tag, place
from datetime import datetime, timedelta
from drf_extra_fields.fields import Base64ImageField


class postSerializer(serializers.ModelSerializer):
    photo = Base64ImageField()

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

    def create(self, validated_data):
        posting = post.objects.create(
            user_id=validated_data['user_id'],
            place_id=validated_data['place_id'],
            mood_status=validated_data['mood_status'],
            title=validated_data['title'],
            content = validated_data['content'],
            mood_tag=validated_data['mood_tag'],
            photo=validated_data['photo']
        )
        posting.save()
        return posting

class placeSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ['id', 'explanation', 'place_name', 'lat', 'lng', 'place_tag', 'photo']
        
class placeTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = place_tag
        fields = '__all__'

class moodStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = mood_status
        fields = '__all__'