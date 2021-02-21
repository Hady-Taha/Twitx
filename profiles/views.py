from django.shortcuts import render,redirect
from .models import Profile,RelationShip,Notification
from .forms import ProfileSetting
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from posts.models import Post
# Create your views here.


def profiles(request, slug):
    if request.user.is_authenticated==False:
        return redirect('twitx')
    user = request.user.profile
    profile = Profile.objects.get(slug=slug)
    posts = Post.objects.filter(user=profile).order_by('-created')
    not_ = Notification.objects.filter(receiver=profile, is_seen=False)
    if request.method == 'POST':
        if profile.user in user.follow.all():
            user.follow.remove(profile.user)
        else:
            user.follow.add(profile.user)
        #done add profiles To Following
        ###############################
        #now add to RelationShip models
        follows, created = RelationShip.objects.get_or_create(sender=user, receiver=profile)
        if created == False:
            if follows.status == 'following':
                follows.status = 'UnFollow'
            else:
                follows.status = 'following'
        else:
            follows.status = 'following'
        user.save()
        follows.save()
    
    
    context={
        'title': f'Profile / {profile.user}',
        'profile': profile,
        'not_': not_,
        'posts':posts,
        
    }
    return render(request, 'profiles/profiles.html', context)


def settings(request, slug):
    if request.user.username != slug:
        return redirect('home')
    profile = Profile.objects.get(slug=slug)
    form = ProfileSetting(request.POST or None,request.FILES or None, instance=profile)
    if form.is_valid():
        form.save()
    context = {
        'title': 'settings',
        'profile': profile,
        'form':form,
        
    }
    return render(request, 'profiles/settings.html', context)


def notification(request, slug):
    if request.user.username != slug:
        return redirect('home')
    profile = Profile.objects.get(slug=slug)
    not_ = Notification.objects.filter(receiver=profile,is_seen=False).order_by('-created')
    if request.method == 'POST':
        Notification.objects.filter(receiver=profile, is_seen=False).update(is_seen=True)
    context = {
        'title': 'notification',
        'not_':not_,
    }
    return render(request, 'profiles/notification.html', context)



def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = UserCreationForm()
    posts = Post.objects.all().order_by('?')[:1]
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            login(request, user)
            username=form.cleaned_data['username']
            return redirect(f'/profile/{username}')

    else:
        form = UserCreationForm()
    context = {
        'title': 'Register',
        'form':form,
        'posts':posts,
    }
    return render(request,'profiles/register.html',context)


def authentication(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = AuthenticationForm()
    posts = Post.objects.all().order_by('?')[:1]
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                print(user)
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    context = {
        'title': 'Login',
        'form':form,
        'posts':posts,
    }
    return render(request,'profiles/login.html',context)


def vlogout(request):
    logout(request)
    context = {
        'title': 'logout',
    }
    return render(request, 'profiles/logout.html', context)
