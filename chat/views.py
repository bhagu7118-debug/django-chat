from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Automatically log the user in after registering
            return redirect('/') # Redirect to the home page (we will build this later)
    else:
        form = UserCreationForm()
    
    return render(request, 'registration/register.html', {'form': form})

def index(request):
    return render(request, 'chat/index.html')