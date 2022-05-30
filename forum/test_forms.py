from django.test import TestCase
from .forms import PostitForm, PostitComments


class TestPostitForm(TestCase):

    def test_postit_heading_is_required(self):
        form = PostitForm({'heading': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('heading', form.errors.keys())
        self.assertEqual(form.errors['heading'][0], 'This field is required.')
    
    def test_link_field_is_not_required(self):
        form = PostitForm({'heading': 'Test Postit Form'})
        self.assertFalse(form.is_valid())
    
    def test_form_input_fields_are_in_metaclass(self):
        form = PostitForm()
        self.assertEqual(form.Meta.fields, ['heading', 'body', 'link'])





# class TestPostitComments(TestCase):
