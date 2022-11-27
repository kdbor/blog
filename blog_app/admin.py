from django.contrib import admin

# from django_summernote.admin import SummernoteModelAdmin
from .models import BlogPost, Feedback
from tinymce.widgets import TinyMCE
from django.db import models


# Apply summernote to all TextField in model.
@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    exclude = ("slug",)
    list_display = ("id", "title", "category", "date_created")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    list_per_page = 25
    formfield_overrides = {models.TextField: {"widget": TinyMCE()}}


# admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Feedback)
