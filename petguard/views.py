from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Animal
# Login
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")  # nome da URL da página principal
        else:
            messages.error(request, "Usuário ou senha inválidos")
    return render(request, "petguard/login.html")


# Logout
def logout_view(request):
    logout(request)
    return redirect("login")


# Página principal protegida
@login_required(login_url="login")
def index(request):
    return render(request, "petguard/index.html")

def detalhes(request, id):
    animal = get_object_or_404(Animal, id=id)
    return render(request, "petguard/detalhes.html", {"animal": animal})
