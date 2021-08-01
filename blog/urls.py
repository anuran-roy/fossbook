from django.urls import path, include
from . import views, feeds

urlpatterns = [
    # path('', views.index, name="Index"),
    path('', views.PostList.as_view(), name='home'),
    path("feed/rss", feeds.RSSFeed(), name="rss_feed"),
    path("feed/atom", feeds.AtomFeed(), name="atom_feed"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post'),
]