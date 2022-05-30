from django.test import TestCase
from .models import Postit


class TestModels(TestCase):

    def test_thread_starter_default_to_true(self):
        postit = Postit.objects.create()
        self.assertTrue(postit.thread_starter)
