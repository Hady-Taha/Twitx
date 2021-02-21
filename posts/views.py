from django.shortcuts import render,redirect
from .models import Post, Like
from profiles.models import Profile,Notification
from .forms import AddPost
from django.http import JsonResponse
from django.db.models import Q
# Create your views here.


def twitx(request):
    posts = Post.objects.all().order_by('?')
    context = {
        'title': 'twitx',
        'posts': posts,
    }
    return render(request, 'posts/randomPost.html', context)

def home(request):
    if request.user.is_authenticated==False:
        return redirect('twitx')
    form = AddPost()
    posts = Post.objects.filter(Q(user=request.user.profile) | Q(user__in=request.user.profile.get_all_following_posts)).order_by('-created')
    if request.method == 'POST':
        form = AddPost(request.POST)
        if form.is_valid():
            newPost = form.save(commit=False)
            newPost.user = request.user.profile
            newPost.save()
            form = AddPost()
    context = {
        'title': 'Home',
        'posts': posts,
        'form': form,
    }
    return render(request, 'posts/home.html', context)
    pass


def like_unlike(request):
    user = request.user.profile
    
    if request.method == 'POST':
        postID = request.POST.get('post_id')
        getPost = Post.objects.get(id=postID)
        if user in getPost.liked.all():
            getPost.liked.remove(user)
        else:
            getPost.liked.add(user)



    like, created = Like.objects.get_or_create(user=user, post=getPost)
    if created == False:
        if like.value == 'Like':
            like.value = 'UnLike'
        else:
            like.value = 'Like'
    else:
        like.value='Like'
        
        
    
    like.save()
    getPost.save()
    
    return JsonResponse({'data': getPost.get_all_likes_count()}, status=200)
    
