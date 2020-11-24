from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Post, PostImage 

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "TEMPLATE_NAME"

def detailPostView(request, id)
  post = get_object_or_404(Post, id)
  photos = PostImage.objects.filter(post=post)
  return render(request, 'post-detail', {'photos':photos, 'post':post})




