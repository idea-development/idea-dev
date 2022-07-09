import django_on_heroku
from decouple import config

from .base import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'idea-development.herokuapp.com', 'www.ideadev.co.uk', 'ideadev.co.uk'
]

django_on_heroku.settings(locals())