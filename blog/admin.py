from django.contrib import admin
from .models import Post
from django_summernote.admin import SummernoteModelAdmin
from .models import Post
# Register your models here.

class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'updated_on', 'created_on', 'status')
    list_filter = ("status","updated_on","created_on")
    search_fields = ['title', 'content']
    prepopulated_fields = {
        'slug': ('title',),
        'seo_title': ('title',),
        'seo_description': ('description',)
    }

    summernote_fields = ('content',)

admin.site.register(Post, PostAdmin)
