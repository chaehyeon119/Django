from django.contrib import admin
from journal.models import Journalist
from journal.models import Post
from journal.models import Comment


# admin.site.register(Post)


@admin.register(Journalist)
class JournalistAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at","updated_at"]

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["journallist", "title", "content", "photo",  "created_at","updated_at"]
# Register your models here.

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["post",  "content", "photo",  "created_at","updated_at"]
