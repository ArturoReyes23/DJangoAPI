from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

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
            messages.error(request,'Invalid Login Credentials')
    return render (request,template_name)

# View for Register
def register_view(request):
    template_name = "auth-register.html"
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')

        """print(username)
        print(email)
        print(password)
        print(password_confirmation)"""
        
        if password != password_confirmation:
            messages.error(request, 'Las contraseñas no coinciden')
            return render(request, template_name)

        if User.objects.filter(username=username).exists():
            messages.error(request, 'El usuario ya existe')
            return render(request, template_name)
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya existe')
            return render(request, template_name)

        user = User(
            username=username,
            email=email,
            password=make_password(password)
        )
        user.save()
        messages.success(request, 'Usuario creado con éxito')
    return render (request,template_name)

# View for Forgot the Password
def forgot_view(request):
    template_name = "auth-forgot-password.html"
    
    return render (request,template_name)

# View for logout
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirecciona a la página de login

