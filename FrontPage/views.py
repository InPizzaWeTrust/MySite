from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

from django.http import HttpResponse


def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'frontpage/index.html', {'posts': posts})


def post_detail(request,pk):
    Post.objects.get(pk=pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'frontpage/post_detail.html', {'post': post})


# Create your views here.
