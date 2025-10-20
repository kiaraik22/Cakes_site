from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models.expressions import result
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from blog.models import Posts, Profile
from .forms import CommentsForm

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
    post = get_object_or_404(Posts, pk=pk)
    comments = post.comments_set.all().select_related('owner')  # оптимизация

    # Форма и обработка только для авторизованных
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentsForm(request.POST)
            if form.is_valid():
                try:
                    review = form.save(commit=False)
                    review.owner = request.user.profile  # убедитесь, что профиль существует
                    review.post = post
                    review.save()
                    messages.success(request, "Ваш комментарий добавлен!")
                    return redirect('post_detail', pk=post.pk)
                except Profile.DoesNotExist:
                    messages.error(request, "У вашего аккаунта нет профиля. Обратитесь к администратору.")
                    # или создайте профиль автоматически
        else:
            form = CommentsForm()
    else:
        form = None  # форма не отображается для анонимов

    context = {
        'post': post,
        'comments': comments,
        'form': form,  # будет None для анонимов
    }
    return render(request, 'blog/blog-details.html', context)