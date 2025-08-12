from django.shortcuts import render ,  redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth import get_user_model
# Create your views here.

User = get_user_model()

def login_view(request):
    if (request.method == 'POST'):
        if request.user.is_authenticated:
            return redirect('/')
        username = request.POST.get('username') or None 
        password = request.POST.get('password') or None 
        if all([username, password]) :
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
    return render(request, "auth/login.html", {})

def register_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            return redirect('/')
        username = request.POST.get('username') or None 
        email = request.POST.get('email') or None 
        password = request.POST.get('password') or None 
        
        # django forms in future 
        
        # username_exists = User.objects.filter(username__iexact=username).exists()
        # email_exists = User.objects.filter(email__iexact=email).exists()
        try:
            User.objects.create_user(username=username, email=email, password=password)
            return redirect('/auth/login/')
        except Exception as e:
            pass
    return render(request, "auth/register.html", {})