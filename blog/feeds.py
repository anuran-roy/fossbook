from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import Post
from django.urls import reverse
from django.utils.feedgenerator import Atom1Feed

class AtomFeed(Feed):
    feed_type = Atom1Feed

    title = "FOSSBook blog"
    link = ""
    description = "Posts from the FOSSBook blog."

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)

class RSSFeed(Feed):
    title = "FOSSBook blog"
    link = ""
    description = "Posts from the FOSSBook blog."

    def items(self):
        return Post.objects.filter(status=1)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return truncatewords(item.content, 30)