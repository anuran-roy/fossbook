from django.db import models
from django.contrib.auth.models import User
# from taggit import TaggableManager

# Create your models here.

STATUS = (
    (0, 'draft'),
    (1, 'published')
)

class Post(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(default='', max_length=250)
    slug = models.SlugField(unique=True, max_length=200)
    content = models.TextField(default='Post under work. Please check back sometime later.')
    author = models.ForeignKey(User, on_delete= models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    seo_title = models.CharField(default='Draft Post', max_length=250)
    seo_description = models.TextField(default='', max_length=250)

    # tags = TaggableManager()

    def __str__(self):
        return self.title

    def __slug__(self):
        return self.slug
    
    def __content__(self):
        return self.content
    
    def __tags__(self):
        return self.tags

    class Meta:
        ordering = ['-created_on', '-updated_on', '-author', '-title']