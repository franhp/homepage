from dateutil import parser
from django.conf import settings
from django.core.cache import cache
import requests
from requests_oauthlib import OAuth1Session


class GithubProject():
    def __init__(self, clone_url=None, name=None,
                 description=None, language=None):
        self.clone_url = clone_url
        self.name = name
        self.description = description
        self.language = language


class Tweet():
    def __init__(self, text=None, date=None, status_id=None):
        tweet = []
        for word in text.split():
            if word.startswith('#'):
                tag = '<a href="https://twitter.com/hashtag/%s">%s</a>'
                tweet.append(tag % (word[1:], word))
            elif word.startswith('@'):
                tag = '<a href="https://twitter.com/%s">%s</a>'
                handle = word[1:-1] if word.endswith(':') else word[1:]
                tweet.append(tag % (handle, word))
            elif word.startswith('http://') or word.startswith('https://'):
                tweet.append('<a href="%s">%s</a>' % (word, word))
            else:
                tweet.append(word)
        self.text = ' '.join(tweet)
        self.date = parser.parse(date).strftime('%d %b %Y')
        self.status_id = status_id


class Song():
    def __init__(self, name=None, artist=None, date=None, image=None):
        self.name = name
        self.artist = artist
        self.date = date
        self.image = image


class Github():
    def __init__(self):
        pass

    def fetch(self):
        result = cache.get('github', [])
        if not result:
            r = requests.get('https://api.github.com/users/franhp/repos')
            for project in sorted(r.json(),
                                  key=lambda x: x['pushed_at'],
                                  reverse=True):
                # Discard forks
                if project['fork'] is not True:
                    p = GithubProject(clone_url=project['clone_url'],
                                      name=project['name'],
                                      description=project['description'],
                                      language=project['language'])
                    result.append(p)
            cache.set('github', result)
        return result


class Twitter():
    def __init__(self):
        pass

    def fetch(self):
        result = cache.get('twitter', [])
        if not result:
            twitter = OAuth1Session(settings.TWITTER_CLIENT_KEY,
                                    client_secret=settings.TWITTER_CLIENT_SECRET)
            r = twitter.get('https://api.twitter.com/1.1/statuses/user_timeline.json?screen_name=franhp')
            for tweet in r.json()[0:9]:
                t = Tweet(text=tweet['text'],
                          date=tweet['created_at'],
                          status_id=tweet['id'])
                result.append(t)
            cache.set('twitter', result)
        return result


class Lastfm():
    def __init__(self):
        pass

    def fetch(self):
        result = cache.get('lastfm', [])
        if not result:
            params = {'method': 'user.getrecenttracks',
                      'user': 'franhp',
                      'api_key': settings.LASTFM_KEY,
                      'format': 'json'}
            headers = {'Content-type': 'application/x-www-form-urlencoded'}
            r = requests.post('http://ws.audioscrobbler.com/2.0/?',
                              data=params,
                              headers=headers)
            for track in r.json()['recenttracks']['track']:
                song = Song(artist=track['artist']['#text'],
                            name=track['name'],
                            image=track['image'][1]['#text'])
                try:
                    song.date = track['date']['#text']
                except KeyError:
                    song.date = 'now playing'
                result.append(song)
            cache.set('lastfm', result)
        return result

