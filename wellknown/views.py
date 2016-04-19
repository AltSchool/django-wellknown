from django.http import HttpResponse, Http404
from wellknown.models import Resource

def handle(request, path, *args, **kwargs):

    try:
        r = Resource.objects.get(path=path)
        content = r.content
        content_type = r.content_type
    except Resource.DoesNotExist:
           raise Http404('Resource %s does not exist.' % path)

    return HttpResponse(content or '', content_type=content_type)
