from rest_framework import serializers


class GithubProjectSerializer(serializers.Serializer):
    clone_url = serializers.CharField(max_length=200)
    name = serializers.CharField(max_length=200)
    language = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=300)


class TwitterSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=300)
    date = serializers.CharField(max_length=50)
    status_id = serializers.CharField(max_length=100)


class LastfmSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    artist = serializers.CharField(max_length=200)
    date = serializers.CharField(max_length=50)
    image = serializers.CharField(max_length=200)
