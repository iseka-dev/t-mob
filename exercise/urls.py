from django.urls import path
from . import views

urlpatterns = [
    path(
        'get_redirect/',
        views.get_redirect,
        name='get_redirect',
    ),
]
