from django.views.generic.base import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from models import Github, Lastfm, Twitter
from serializers import GithubProjectSerializer, TwitterSerializer, LastfmSerializer


class ContactView(TemplateView):
    template_name = 'contact.html'

    def get_context_data(self, **kwargs):
        return TemplateView.get_context_data(self, **kwargs)


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        return TemplateView.get_context_data(self, **kwargs)


class GithubAPIView(APIView):
    def get(self, request, *args, **kwargs):
        g = Github()
        serializer = GithubProjectSerializer(g.fetch(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class TwitterAPIView(APIView):
    def get(self, request, *args, **kwargs):
        t = Twitter()
        serializer = TwitterSerializer(t.fetch(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LastfmAPIView(APIView):
    def get(self, request, *args, **kwargs):
        l = Lastfm()
        serializer = LastfmSerializer(l.fetch(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
