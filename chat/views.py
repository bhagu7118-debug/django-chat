from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify
from .models import Room, Message

# 1. THE FORM: Now includes Email and styled fields for the UI
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Required for password recovery.")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

# 2. THE LOBBY: Egalitarian design - any user can create a room
@login_required
def index(request):
    if request.method == 'POST':
        room_name = request.POST.get('room_name', '').strip()
        if room_name:
            # update_or_create ensures we don't get duplicates
            Room.objects.update_or_create(
                name=room_name, 
                defaults={'slug': slugify(room_name)}
            )
            return redirect('index')

    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {'rooms': rooms})

# 3. THE ROOM: Fetches history and handles missing rooms
@login_required
def room(request, slug):
    # Use get_object_or_404 so the app doesn't crash on bad URLs
    room = get_object_or_404(Room, slug=slug)
    
    # Fetch recent history
    messages = Message.objects.filter(room=room).order_by('-date_added')[:50]
    # Reverse them so the oldest is at the top of the chat log
    messages = reversed(messages)

    return render(request, 'chat/room.html', {
        'room': room,
        'messages': messages
    })

# 4. REGISTRATION: Updated template path to match your folder structure
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Auto-login after registration
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'chat/register.html', {'form': form})

# 5. LOGOUT: Standard logout
def logout_view(request):
    logout(request)
    return redirect('login')