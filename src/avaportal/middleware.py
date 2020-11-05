import logging
from urllib.parse import urlsplit, urlunsplit
from django.conf import settings
from django.http import HttpResponseRedirect
from django.utils.deprecation import MiddlewareMixin
from django.middleware.security import SecurityMiddleware


logger = logging.getLogger(__name__)


class GoToHTTPSMiddleware(MiddlewareMixin):
    """
    Force all requests to use HTTPs when behind a reverse proxy.

    .. note::
        ``settings.GO_TO_HTTPS`` needs to be True.
        The RP need to inform HTTP_X_FORWARDED_PROTO and HTTP_X_FORWARDED_HOST.
    """
    def process_request(self, request):
        if getattr(settings, 'GO_TO_HTTPS', False):
            meta = request.META
            if 'HTTP_X_FORWARDED_PROTO' in meta and meta['HTTP_X_FORWARDED_PROTO'] == 'http':
                return HttpResponseRedirect("https://" + meta['HTTP_X_FORWARDED_HOST'] + meta['PATH_INFO'])
