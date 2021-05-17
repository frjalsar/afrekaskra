# manage.py command to clear cache
# python manage.py clearcache

from django.core.management.base import BaseCommand, CommandError
from django.core.cache import cache

class Command(BaseCommand):
    help = 'Clear the cache'

    def handle(self, *args, **options):
        cache.clear()
        self.stdout.write(self.style.SUCCESS('Successfully cleared cache'))