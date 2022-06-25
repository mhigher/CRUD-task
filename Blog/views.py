from dataclasses import field
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import Post
# Create your views here.

class PostCreateView (CreateView):
    model = Post

    fields = [
        '__all__'
    ]
    template_name = 'base.html'
    success_url = 'reverse_lazy(“blog:all”)'

class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'
        
class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class PostUpdateView(UpdateView):
    model = Post
    fields: '__all__'
    success_url = 'reverse_lazy(“blog:all”)'

class PostDeleteView(DeleteView):
    model = Post
    field = '__all__'
    template_name = 'post_confirm_delete.html'
    success_url = 'reverse_lazy(“blog:all”)'

