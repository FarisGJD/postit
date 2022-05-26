'''Database'''

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Category(models.Model):
    '''User generated category model dervied from the Postit model'''
    category = models.CharField(max_length=50)
    slug = models.SlugField(max_length=300, unique=True, blank=True)

    def __str__(self):
        return str(self.category)


class Postit(models.Model):
    '''Django database model for post creation'''
    thread_starter = models.BooleanField(default=True)
    heading = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts"
        )
    generated_on = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    link = models.URLField(max_length=200, null=True, blank=True)
    image = CloudinaryField('image')
    topic = models.ManyToManyField(
        Category, related_name='generated_category', blank=True
        )
    votes = models.ManyToManyField(User, related_name='post_votes', blank=True)

    class Meta:
        '''Orders Posts based on date & time generated'''
        ordering = ['-generated_on']

    def __str__(self):
        return str(self.heading)

    def upvote_count(self):
        '''Returns number of likes'''
        return self.votes.count()


class Reply(models.Model):
    '''User reply to commnets'''
    postit = models.ForeignKey(
        Postit, on_delete=models.CASCADE, related_name='reply_comments'
        )
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_reply'
        )
    comments = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        '''Organises commnets in asending order'''
        ordering = ['date_created']

    def _str_(self):
        return f"Comment {self.comments} by {self.username}"


class Comment(models.Model):
    '''User inital comments to post'''
    postit = models.ForeignKey(
        Postit, on_delete=models.CASCADE, related_name='comments'
        )
    username = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comment'
        )
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    replies = models.ManyToManyField(Reply, blank=True)

    class Meta:
        '''Organises commnets in asending order'''
        ordering = ['date_created']

    def _str_(self):
        return f"Comment {self.comment} by {self.username}"
