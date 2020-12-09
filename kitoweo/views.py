def welcome(request):
from django.http  import HttpResponse
from django.shortcuts import render, redirect
from django.http  import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from .forms import RegisterForm, PostForm,UpdateUserForm,UpdateProfileForm,
from .models import Post,Profile, User,Rate
from django.db.models import Avg
import math
import random

# Create your views here.

def index(request):
    return render(request, '', context)

def home(request):
    posts = Post.objects.all().order_by("-posted")
    if request.method == 'POST':
        uform = PostForm(request.POST, request.FILES)
        if uform.is_valid():
            post = uform.save(commit=False)
            post.user = request.user
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        uform = PostForm()
    return render(request, '',{'uform': uform,'posts':posts})
    

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, '', {'form': form})

@login_required(login_url='login')
def profile(request, username):
    return render(request, '')


@login_required(login_url='login')
def edit_profile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return redirect('profile', user.username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateProfileForm(instance=request.user.profile)
    params = {
        'user_form': user_form,
        'prof_form': prof_form
    }
    return render(request, 'edit.component.html', params)
    
