from django.contrib import admin
from .models import Postit, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Postit)
class PostitAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('heading',)}
    list_filter = ['generated_on']
    search_fields = ['heading', 'content']
    list_display = ('heading', 'slug', 'generated_on')
    summernote_fields = ('body')


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):

    list_filter = ('approved', 'date_created')
    search_fields = ['username', 'comment']
    list_display = (
        'username', 'comment', 'postit', 'date_created', 'approved'
        )
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
