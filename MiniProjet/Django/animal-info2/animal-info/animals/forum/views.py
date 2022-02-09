from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
    all_posts = Post.objects.all()
    if request.method == 'POST':
        comment= request.POST.get('comment')
        new_post = Post(text=comment, author=request.user)
        new_post.save()
        return redirect('forum_home')
    return render(request, 'forum.html', {'posts':all_posts})