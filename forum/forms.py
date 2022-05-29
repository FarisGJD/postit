from django import forms 
from .models import Postit, Comment


class PostitForm(forms.ModelForm):
    class Meta:
        model = Postit
        fields = [
            'heading',
            'body',
            'link',
            'image',
        ]


class PostitComments(forms.ModelForm):
    class Meta: 
        model = Comment
        fields = ('comment', )