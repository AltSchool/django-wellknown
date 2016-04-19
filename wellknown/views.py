from django.http import (
    HttpResponse,
    HttpResponseForbidden,
    HttpResponseNotFound,
)
from wellknown.models import Resource


def handle(request, path, *args, **kwargs):
    if request.method != 'GET':
        return HttpResponseForbidden('Only GET allowed.')

    try:
        r = Resource.objects.get(path=path)
        content = r.content
        content_type = r.content_type
    except Resource.DoesNotExist:
        return HttpResponseNotFound('Resource %s does not exist.' % path)

    return HttpResponse(content or '', content_type=content_type)
