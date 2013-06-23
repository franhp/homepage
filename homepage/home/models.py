import requests
import base64
from django.core.cache import cache
from django.conf import settings


class Song():
    name = ''
    artist = ''
    date = ''
    image = ''


class Lastfm():
    songs = []

    def grabSongs(self):
        self.songs = cache.get('lastfm', [])
        if len(self.songs) is 0:
            try:
                params = {'method': 'user.getrecenttracks',
                          'user': 'franhp',
                          'api_key': settings.LASTFM_KEY,
                          'format': 'json'}
                headers = {'Content-type': 'application/x-www-form-urlencoded'}
                r = requests.post('http://ws.audioscrobbler.com/2.0/?', data=params, headers=headers)
                response = r.json()
                for track in response['recenttracks']['track']:
                    song = Song()
                    song.artist = track['artist']['#text']
                    song.name = track['name']
                    try:
                        song.date = track['date']['#text']
                    except KeyError:
                        song.date = 'now playing'
                    song.image = track['image'][1]['#text']
                    self.songs.append(song)
                cache.set('lastfm', self.songs)
            except Exception:
                return []
        return self.songs


class GithubProject():
    name = ''
    language = ''
    clone_url = ''
    description = ''


class Github():
    projects = []

    def grabProjects(self):
        self.projects = cache.get('github', [])
        if len(self.projects) is 0:
            try:
                r = requests.get('https://api.github.com/users/franhp/repos')
                response = r.json()

                for i in response:
                    project = GithubProject()
                    project.clone_url = i['clone_url']
                    project.name = i['name']
                    project.description = i['description']
                    project.language = i['language']
                    self.projects.append(project)
                self.projects.reverse()
                cache.set('github', self.projects)
            except Exception:
                return []

        return self.projects


class Tweet():
    text = ''
    date = ''
    source = ''


class Twitter():
    tweets = []

    def grabTweets(self):
        self.tweets = cache.get('twitter', [])
        if len(self.tweets) is 0:
            try:
                url = 'https://api.twitter.com'

                # Request token
                auth = settings.TWITTER_KEY+':'+settings.TWITTER_SECRET
                headers = {'Authorization': 'Basic ' + base64.b64encode(auth),
                           'Content-type': 'application/x-www-form-urlencoded'}
                payload = {'grant_type': 'client_credentials'}
                r1 = requests.post(url + '/oauth2/token', data=payload, headers=headers)
                token = r1.json()['access_token']
                
                # Request tweets
                headers = {'Authorization': 'Bearer ' + token}
                r2 = requests.get(url + '/1.1/statuses/user_timeline.json?screen_name=franhp', headers=headers)
                response = r2.json()

                for i in response:
                    tweet = Tweet()
                    tweet.text = i['text']
                    tweet.source = i['source']
                    tweet.date = i['created_at']
                    self.tweets.append(tweet)
                cache.set('twitter', self.tweets)
            except Exception:
                return []

        return self.tweets
