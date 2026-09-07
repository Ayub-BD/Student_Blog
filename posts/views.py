from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from .models import Post, Message

def index(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})

def post(request, post_id):
    post_item = get_object_or_404(Post, id=post_id)
    return render(request, 'posts.html', {'post': post_item})

def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print("User created successfully", user.username)
            return redirect('login')
        else:
            print("REGISTRATION ERRORS:", form.errors)
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        body = request.POST.get('body')
        pdf_file = request.FILES.get('pdf_file')
        driver_link = request.POST.get('driver_link')
        document_link = request.POST.get('document_link')

        if title and body:
            Post.objects.create(
                title=title,
                body=body,
                pdf_file=pdf_file,
                driver_link=driver_link,
                document_link=document_link,
                author=request.user
            )
            return redirect('index')
    return render(request, 'create.html')

@login_required
def delete_post(request, post_id):
    post_item = get_object_or_404(Post, id=post_id)
    
    if post_item.author == request.user or request.user.is_superuser:
        post_item.delete()
    return redirect('index')

@login_required
def search_users(request):
    query = request.GET.get('q', '')
    results = []
    if query:
        results = User.objects.filter(username__icontains=query).exclude(id=request.user.id)
    return render(request, 'user_search.html', {'query': query, 'results': results})

# --- আপডেট করা চ্যাট ভিউ ---
@login_required
def chat_view(request, username=None):
    if not username:
        return redirect('search_users')
    
    other_user = get_object_or_404(User, username=username)
    
    # রুম নেম জেনারেট (যেমন: 1_2)
    user_ids = sorted([request.user.id, other_user.id])
    room_name = f"{user_ids[0]}_{user_ids[1]}"
    
    # ২ জন ইউজারের সব মেসেজ ডাটাবেজ থেকে লোড করা
    chat_messages = Message.objects.filter(
        (Q(sender=request.user) & Q(receiver=other_user)) |
        (Q(sender=other_user) & Q(receiver=request.user))
    ).order_by('timestamp')

    # Unread মেসেজগুলো Read মার্ক করা
    Message.objects.filter(sender=other_user, receiver=request.user, is_read=False).update(is_read=True)

    return render(request, 'chat.html', {
        'room_name': room_name,
        'other_user': other_user,
        'chat_messages': chat_messages
    })
