from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.cache import cache

# Create your models here.


class Redirect(models.Model):
    key = models.CharField(max_length=100, unique=True, db_index=True)
    url = models.CharField(max_length=1000)
    active = models.BooleanField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @receiver(post_save, sender='exercise.Redirect')
    def cache_active(sender, instance, created, **kwargs):
        cache.clear()
        active = Redirect.objects.filter(active=True).values()
        for a in active:
            cache.set(a['key'], a['url'])
