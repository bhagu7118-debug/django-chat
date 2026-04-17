from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Room, Message

# 1. THE FORM: Required for all users
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

# 2. THE LOBBY: Anyone logged in can create a room
@login_required
def index(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name')
        if room_name:
            # This creates a room for ANY logged-in user
            Room.objects.update_or_create(
                name=room_name, 
                defaults={'slug': slugify(room_name)}
            )
            return redirect('index')

    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})

# 3. THE ROOM: Anyone logged in can join
@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = room.messages.all()[0:50] 
    return render(request, 'chat/room.html', {'room': room, 'messages': messages})

# 4. REGISTRATION: Standard for everyone
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form': form})

# 5. LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')