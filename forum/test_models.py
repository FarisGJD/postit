from django.test import TestCase
from .models import Postit 


class TestModels(TestCase):

    def test_thread_starter_default_to_true(self):
        postit = Postit.objects.create()
        self.assertTrue(postit.thread_starter)
    
    # def test_item_string_method_returns_name(self):
    #     postit = Postit.objects.create(heading='Test Postit')
    #     self.assertEqual(str(postit), 'Test Postit')
