from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

CATEGORY = []


class Postit(models.Model):
    '''Django database model for post creation'''
    thread_starter = models.BooleanField(default=True)
    heading = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    generated_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    link = models.URLField(max_length=200, unique=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    category = models.CharField(max_length=15, choices=CATEGORY)
    votes = models.ManyToManyField(User, related_name='thread_votes', blank=True)

    class Meta:
        '''Orders Posts based on date & time generated'''
        ordering = ['-generated_on']

    def __str__(self):
        return str(self.heading)

    def upvote_count(self):
        return self.votes.count()
    
    def _selected_category(self):
        return str(self.category)

