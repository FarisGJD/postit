from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Postit(models.Model):
    '''Django database model for post creation'''
    thread_starter = models.BooleanField(default=True)
    heading = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="forum_posts")
    generated_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    link = models.URLField(max_length=200, bull=True, blank=True)
    image = CloudinaryField('image', default='placeholder')
    topic = models.CharField(max_length=20, unique=True)
    votes = models.ManyToManyField(User, related_name='post_votes', blank=True)

    class Meta:
        '''Orders Posts based on date & time generated'''
        ordering = ['-generated_on']

    def __str__(self):
        return str(self.heading)

    def upvote_count(self):
        return self.votes.count()


class Categories(models.Model):
    '''User generated category model dervied from the Postit model''' 
    category = models.ManyToManyField(Postit, related_name='user_categories', blank=True)

    def list_of_categories(self):
        return self.category


class Reply(models.Model):
    '''User reply to commnets'''
    postit = models.ForeignKey(Postit, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_reply')
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def _str_(self):
        return f"Comment {self.comment} by {self.username}"


class Comments(models.Model):
    '''User inital comments to post''' 
    postit = models.ForeignKey(Postit, on_delete=models.CASCADE, related_name='comments')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    replies = models.ManyToManyField(Reply, blank=True)

    class Meta:
        ordering = ['created_on']

    def _str_(self):
        return f"Comment {self.comment} by {self.username}"

