from django.contrib import admin
from .models import Postit, Comment, Reply, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Postit)
class PostitAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('heading',)}
    list_filter = ('generated_on', 'topic')
    search_fields = ['heading', 'content', 'topic']
    list_display = ('heading', 'slug', 'generated_on')
    summernote_fields = ('body')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    search_fields = ['category']
    prepopulated_fields = {'slug': ('category', )}


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


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_filter = ['date_created']
    search_fields = ['username', 'comment']
    list_display = (
        'username', 'comment', 'postit', 'date_created'
        )
