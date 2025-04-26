from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Post, Profile
from .forms import CreatePost, UpdateProfile, UpdateUserForm, Registration,Login
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def home(request):
    all_post = Post.objects.all().order_by("-date_modified")
    all_users = User.objects.exclude(id=request.user.id)
    
    if request.method == "POST":
        create_post = CreatePost(request.POST or None)
        if create_post.is_valid():
            post = create_post.save(commit=False)
            post.user_post = request.user
            post.save()
            messages.success(
                request,
                f"New feed has been created by {post.user_post.first_name} {post.user_post.last_name}",
            )
            return redirect("index")
    else:
        create_post = CreatePost()
    content = {"all": all_post, "users": all_users, "add_post": create_post}
    return render(request, "index.html", content)

@login_required(login_url='login')
def edit_post(request, post):
    get_post = Post.objects.get(pk=post)

    if request.method == "POST":
        edit_post = CreatePost(request.POST, instance=get_post)
        if edit_post.is_valid():
            post = edit_post.save(commit=False)
            post.user_post = request.user
            post.save()
            messages.success(request, f"Feed has been edited by successfully")
            return redirect("index")
    else:
        edit_post = CreatePost(instance=get_post)
    content = {"get": get_post, "post": edit_post}
    return render(request, "edit_post.html", content)


@login_required(login_url='login')
def profile(request):
    my_profile = get_object_or_404(Profile, user=request.user)

    context = {"profile": my_profile}
    return render(request, "profile.html", context)


@login_required(login_url='login')
def check_profile(request, pk):
    my_profile = get_object_or_404(Profile, id=pk)

    context = {"profile": my_profile}
    return render(request, "check_profile.html", context)


@login_required(login_url='login')
def update_profile(request):
    user = request.user
    update = get_object_or_404(Profile, user=request.user)
    if request.method == "POST":
        update_user = UpdateUserForm(request.POST or None, instance=user)
        update_form = UpdateProfile(
            request.POST or None, request.FILES or None, instance=update
        )
        if update_user.is_valid() and update_form.is_valid():
            profile = update_form.save(commit=False)
            profile.user = user
            update_user.save()
            profile.save()
            messages.success(request, "Your profile has been updated successfully")
            return redirect("profile")
    else:
        update_user = UpdateUserForm(instance=user)
        update_form = UpdateProfile(instance=update)

    context = {"update_user": update_user, "edit_profile": update_form}
    return render(request, "edit_profile.html", context)


@login_required(login_url='login')
def like_tag(request,liking):
    post = get_object_or_404(Post,id=liking)
    all_likes = post.likes.all()
    if request.user in all_likes:
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    
    return redirect('index')

def registration(request):
    # prevent logged in users from access registration page
    if request.user.is_authenticated:
        return redirect('index')
    register = Registration(request.POST or None)
    if request.method =="POST":
        if register.is_valid():
            register.save()
            messages.success(request,'You have successfully registered')
            return redirect('login')
    
    else:
        register = Registration()
    context = {
        'sign_up':register
    }
    return render(request,'registration.html',context)


class CreateLoginView(LoginView):
    template_name = "login.html"
    authentication_form = Login

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            # If user is authenticated, redirect them to another page
            return redirect('index')  # Adjust the URL as per your project
        return super().dispatch(request, *args, **kwargs)