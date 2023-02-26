from django.views.generic import ListView, DetailView, UpdateView
from django.views.generic.edit import CreateView # new
from .models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class BlogCreateView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = ['name']


class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['name']
