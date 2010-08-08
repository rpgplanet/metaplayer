from os.path import dirname, join, normpath

import django
from django.conf.urls.defaults import *
from django.conf import settings
#from django.views.generic.simple import redirect_to

import ella

ADMIN_ROOTS = (
    normpath(join(dirname(ella.__file__), 'newman', 'media')),
    normpath(join(dirname(django.__file__), 'contrib', 'admin', 'media')),
)

from metaplayer.service import urls as serviceurls
from rpgcommon.user import urls as userurls

urlpatterns = patterns('',
    url(r'^', include(serviceurls, namespace="service")),
    url(r'^', include(userurls, namespace="user")),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        # serve static files
        (r'^%s/(?P<path>.*)$' % settings.STATIC_URL.rstrip('/').lstrip('/'), 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
        # serve static files
        (r'^%s/(?P<path>.*)$' % settings.MEDIA_URL.rstrip('/').lstrip('/'), 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    )



handler404 = 'ella.core.views.page_not_found'
handler500 = 'ella.core.views.handle_error'
