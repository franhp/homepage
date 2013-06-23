from django.shortcuts import render_to_response
from django.template.context import RequestContext
from home.models import Github
from home.models import Twitter
from home.models import Lastfm


def index(request):

    github = Github()
    twitter = Twitter()
    lastfm = Lastfm()

    return render_to_response('home.html', RequestContext(request, {
                                 'twitter': twitter.grabTweets()[0:10],
                                 'github': github.grabProjects()[0:10],
                                 'lastfm': lastfm.grabSongs(),
                                 'location': 'London'}))
