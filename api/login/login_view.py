from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 

# View for Login
def login_views(request):
    template_name = "auth-login.html"
    
    # verifica si el usuario ya está autentificado
    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirecciona a la página principal
        else:
            messages.error(request,'Invalid login credentials')
    return render (request,template_name)

# View for Register
def register_view(request):
    template_name = "auth-register.html"
    
    return render (request,template_name)

# View for Forgot the Password
def forgot_view(request):
    template_name = "auth-forgot-password.html"
    
    return render (request,template_name)

# View for logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirecciona a la página de login

