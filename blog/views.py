from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from django.contrib import messages
from .forms import PostForm, CommentForm, LoginForm, RegisterForm,SubscribeForm
from .models import Post, Category, Tag, Comment, SubComment, User, Subscriber, Profile


def get_categories():
    all = Category.objects.all()
    count = all.count()
    half = count / 2 + count % 2
    first_half = all[:half]
    second_half = all[half:]
    return {'cat_left': first_half, 'cat_right': second_half}


def index(request):
    posts = Post.objects.all().order_by("-published_date")

    context = {'posts': posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


def contacts(request):
    context = {}
    return render(request, "blog/contact.html", context)


def post_detail(request,slug=None):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
    form = CommentForm()
    comments = Comment.objects.filter(post=post).order_by("-created_at")
    context = {'post': post, 'comments': comments, 'form': form}
    context.update(get_categories())
    return render(request, "blog/post.html", context)


def category(request, slug=None):
    c = get_object_or_404(Category, slug=slug)
    posts = Post.objects.filter(category=c).order_by("-published_date")
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


def posts_by_tag(request, slug=None):
    t = Tag.objects.get(slug=slug)
    posts = Post.objects.filter(tags=t).order_by("-published_date")
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


def search(request):
    qwery = request.GET.get("query")
    posts = Post.objects.filter(Q(content__icontains=qwery) | Q(title__icontains=qwery))
    context = {'posts': posts}
    context.update(get_categories())
    return render(request, "blog/index.html", context)


@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.published_date = now()
            new_post.user = request.user
            new_post.save()
            form.save_m2m()
            return index(request)
    form = PostForm()
    context = {'form': form}
    return render(request, "blog/create.html", context)


def post_edit(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return index(request)
    form = PostForm(instance=post)
    context = {'form': form,
               'post': post}
    return render(request, "blog/edit.html", context)


def post_delete(request, slug=None):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "Successfully deleted post")
    return index(request)


def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, "Невірний логін або пароль")
    else:
        form = LoginForm()

    context = {'form': form}
    return render(request, "registration/login.html", context)


def user_logout(request):
    logout(request)
    return render(request, 'registration/logged_out.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, "Successfully registration ")
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {"form": form})


@login_required
def profile(request):
    user_profile, created = Profile.objects.get_or_create(user=request.user)

    context = {
        'profile_user': request.user,
        'user_profile': user_profile,
    }
    context.update(get_categories())
    return render(request, "blog/user_profile.html", context)


def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")

        if not email:
            messages.error(request, "Введіть email.")
            return redirect('home')

        if Subscriber.objects.filter(email=email).exists():
            messages.warning(request, "Цей email вже підписаний.")
        else:
            Subscriber.objects.create(email=email)
            messages.success(request, "Ви успішно підписалися на новини.")

    return redirect('home')







