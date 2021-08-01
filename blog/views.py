from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>This is the blog index</h1>")

class PostList(ListView):
    # model = Post
    paginate_by = 10
    queryset = Post.objects.filter(status=1).order_by('-updated_on')
    template_name = 'index.html'

class PostDetail(DetailView):
    model = Post
    # queryset = Post.objects.filter(status=1).order_by('-updated_on')
    template_name = 'post.html'
