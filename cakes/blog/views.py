from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.expressions import result
from django.shortcuts import render
from blog.models import Posts

# Create your views here.


def posts(request):
    posts = Posts.objects.all()

    page = request.GET.get('page')
    results = 3
    paginator = Paginator(posts, results)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)

    left_index = int(page) - 3

    if left_index < 1:
        left_index = 1

    right_index = int(page) + 4

    if right_index > paginator.num_pages:
        right_index = paginator.num_pages + 1

    custom_range = range(left_index, right_index)

    context = {'posts':posts, 'custom_range': custom_range, 'paginator': paginator}
    return render(request, 'blog/blog_post.html', context)


def post_detail(request, pk):
    post = Posts.objects.get(pk=pk)
    context = {'post':post}
    return render(request, 'blog/blog-details.html', context)
