from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import RegistrationForm, LoginForm
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Handle registration logic (create user)
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Handle login logic
            return redirect('catalog')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def catalog(request):
    # Retrieve and display product catalog
    return render(request, 'catalog.html')

def cart(request):
    # Display user's shopping cart
    return render(request, 'cart.html')
