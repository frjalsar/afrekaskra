# manage.py command to clear cache
# python manage.py clearcache

from django.core.management.base import BaseCommand, CommandError
from django.core.cache import cache
from django.test import Client

class Command(BaseCommand):
    help = 'Clear the cache'

    def handle(self, *args, **options):
        # Clear the cache
        cache.clear()
        self.stdout.write(self.style.SUCCESS('Successfully cleared cache'))
        cache.close()