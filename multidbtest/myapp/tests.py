from django.contrib.auth.models import User

from django.test import TestCase


class Example(TestCase):
    def test_rollback(self):
        User.objects.create(username='abc')

