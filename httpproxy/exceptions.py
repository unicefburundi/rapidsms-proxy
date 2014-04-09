from django.http import Http404
"""
Some generic exceptions that can occur in Django HTTP Proxy
"""

class UnkownProxyMode(Exception):
    pass


class ResponseUnsupported(Exception):
    pass


class RequestNotRecorded(Http404):
    pass

