from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post

from django.db.models import Q


@login_required
def post_list(request):
    posts = Post.objects.filter(is_active=True).order_by('-created_at')
    query = request.GET.get('search')
    if query:
        posts = posts.filter(
            Q(title__icontains=query) | Q( content__icontains=query )
        )
    context = {
        'posts': posts,
        'query':query
    }
    return render(request, 'post_list.html', context)