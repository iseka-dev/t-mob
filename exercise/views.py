from django.shortcuts import render
from django.core.cache import cache
from django.http import JsonResponse

# Create your views here.


def get_redirect(request):
    key = request.GET.get('key')
    values = cache.get(key)
    print(values)
    return JsonResponse({
        'key': key,
        'url': values,
    })
