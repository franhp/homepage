from fabric.context_managers import shell_env, lcd
from fabric.decorators import task
from fabric.operations import local
from fabric.api import env, put, run, cd
import os

COMMON_SETTINGS = {
                   'DJANGO_CONFIGURATION': 'Development',
                   'DJANGO_SETTINGS_MODULE': 'homepage.settings',
                   'DJANGO_SECRET_KEY': 'secret_key',
                   'DATABASE_URL': None,
                   'LASTFM_KEY': None,
                   'TWITTER_CLIENT_KEY': None,
                   'TWITTER_CLIENT_SECRET': None
                   }


@task
def runserver():
    with shell_env(**COMMON_SETTINGS):
        local('python manage.py runserver 0.0.0.0:8000')

@task
def gunicorn():
    with shell_env(**COMMON_SETTINGS):
        local('gunicorn homepage.wsgi --log-file -')

@task
def watch():
    with lcd('static/foundation'):
        local('bundle exec compass watch')


@task
def compile_css():
    local('echo NOT IMPLEMENTED')


@task
def generate_dotenv():
    with open('.env', 'wb') as f:
        for k in COMMON_SETTINGS.keys():
            var = os.environ.get(k, COMMON_SETTINGS[k])
            print 'Writing %s="%s"' % (k, var)
            f.write('%s="%s"\n' % (k, var))


@task
def restart():
    for host in env.hosts:
        run('touch /home/grap/%s/tmp/restart.txt' % host)


@task
def disable_develop():
    local('echo lol')

@task
def enable_develop():
    local('echo lol')

@task
def pack():
    local('tar zcf ../website.tar.gz * .env', capture=False)

@task
def deploy():
    for host in env.hosts:
        with cd('~/%s' % host):
            put('../website.tar.gz', '~')
            run('rm -rf *')
            run('tar zxvf ~/website.tar.gz')
            run('rm ~/website.tar.gz')

            # Syncdb
            local('python manage.py migrate')
            
            # Force restart
            run('mkdir -p tmp')
            restart()


    # syncdb / migrate