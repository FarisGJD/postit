from django.test import TestCase
from .models import Postit


class TestViews(TestCase):

    def test_get_postit_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    # def test_get_profile_list(self):
    #     response = self.client.get('/profile')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'postit/profile.html')
    
    # def test_get_thread_list(self):
    #     response = self.client.get('/profile')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'profile.html')
    
    # def test_get_create_postit(self):
    #     response = self.client.get('/add')
    #     self.assertEqual(response.status_code, 301)
    #     self.assertTemplateUsed(response, 'postit/create-postit.html')
    
    # def test_get_edit_postit(self):
    #     postit = Postit.objects.create()
    #     response = self.client.get(f'/edit/{postit.id}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'postit/edit-postit.html')
    
    # def test_create_postit(self):
    #     response = self.client.post('/add', {'heading': 'Test Create Post'})
    #     self.assertRedirects(response, 'home')

    # def test_get_delete_postit(self):
    #     postit = Postit.objects.create()
    #     response = self.client.get(f'/delete/{postit.id}')
    #     self.assertRedirects(response, 'delete')
    #     existing_items = Item.objects.filter(id=postit.id)
    #     self.assertEqual(len(existing_postit, 0))