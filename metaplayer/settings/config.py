from os.path import dirname, join

import metaplayer as project

DEBUG = True
TEMPLATE_DEBUG = DEBUG
ENABLE_DEBUG_URLS = DEBUG

FACEBOOK_APPLICATION_ID = '137786606258153'
GOOGLE_ANALYTICS_CODE = 'UA-17874961-1'

STATIC_ROOT = join(dirname(project.__file__), 'static')

ADMIN_MEDIA_PREFIX = '/static/admin_media/'

SECRET_KEY = '^980$0s46q1(toq*mu23m41_ac_@vwy)+mig=ka_97$m0^fh)v'

CACHE_BACKEND = 'dummy://'
CACHE_TIMEOUT = 10*60
CACHE_SHORT_TIMEOUT = 1*60
CACHE_LONG_TIMEOUT = 60*60

NEWMAN_MEDIA_PREFIX = '/static/newman_media/'

SESSION_COOKIE_DOMAIN = '.rpghrac.cz'

