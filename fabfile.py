from fabric.context_managers import shell_env, lcd
from fabric.decorators import task
from fabric.operations import local

COMMON_SETTINGS = {
                   'DJANGO_CONFIGURATION': 'Development',
                   'DJANGO_SETTINGS_MODULE': 'homepage.settings',
                   'DJANGO_SECRET_KEY': 'secret_key',
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
