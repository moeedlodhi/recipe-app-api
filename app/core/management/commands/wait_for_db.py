"""
Django command to wait for the database to be available
"""
from lib2to3.pytree import Base
from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError

class Command(BaseCommand):
    """Django command goes here"""
    def handle(self, *args, **oprions):
        self.stdout.write('Waiting for db')
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('DB unavailable, wait one second')
                time.sleep(1)
            self.stdout.write(self.style.SUCCESS('Database available'))    

