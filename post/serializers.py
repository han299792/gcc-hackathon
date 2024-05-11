from rest_framework import serializers
from post.models import post, mood_status, place_tag, place

class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ['id', 'user_id', 'place_id', 'mood_status', 'title', 'content', 'photo', 'mood_tag']

class placeSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = ['id', 'place_name', 'lat', 'lng', 'place_tag', 'photo']