from django.shortcuts import render
from blog.models import Posts

# Create your views here.


def posts(request):
    posts = Posts.objects.all()

    context = {'posts':posts}
    return render(request, 'blog/blog_post.html', context)


def post_detail(request, pk):
    post = Posts.objects.get(pk=pk)
    context = {'post':post}
    return render(request, 'blog/blog-details.html', context)
