from django.urls import path, include
from . import views

urlpatterns = [
    # path('', views.index, name="Index"),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post'),
]