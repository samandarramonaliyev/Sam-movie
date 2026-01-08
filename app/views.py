from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import Film, Janr
from .forms import FilmForm

# ==========================
# RO'YXATDAN O'TISH & LOGIN
# ==========================
def register_view(request):
    if request.user.is_authenticated:
        return redirect('films')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('films')
    else:
        form = UserCreationForm()
    
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.user.is_authenticated:
        return redirect('films')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('films')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('films')


# ==========================
# FILMLAR
# ==========================
def films(request):
    search = request.GET.get("search")
    films = Film.objects.filter(approved=True)

    if search:
        films = films.filter(name__icontains=search)
    
    return render(request, 'film.html', {
        "films": films,
        "categories": Janr.objects.all()
    })


def film_detail(request, pk):
    film = get_object_or_404(Film, pk=pk)
    actors = [a.strip() for a in film.actor.split(",")] if film.actor else []
    
    return render(request, "film_detail.html", {"film": film, "actors": actors})


def film_category(request, pk):
    janr = get_object_or_404(Janr, pk=pk)
    films = Film.objects.filter(genres=janr, approved=True)
    
    return render(request, "film_category.html", {
        "janr": janr,
        "films": films,
        "categories": Janr.objects.all()
    })


# ==========================
# FILM QO'SHISH
# ==========================
@login_required
def add_film_view(request):
    if request.method == "POST":
        form = FilmForm(request.POST, request.FILES)
        if form.is_valid():
            film = form.save(commit=False)

            # Boolean qiymatni form.cleaned_data dan oling — bu aniq True/False qaytaradi
            anonymous_checkbox = form.cleaned_data.get("anonymous", False)

            # Agar foydalanuvchi login qilgan bo'lsa created_by ni saqlaymiz
            film.created_by = request.user

            # anonymous maydonini form orqali olingan qiymatga moslab o'rnating
            film.anonymous = bool(anonymous_checkbox)

            # approved default holatini xohlaganingizcha belgilang
            film.approved = False

            film.save()
            form.save_m2m()
            return redirect("films")
    else:
        form = FilmForm()

    return render(request, "film_add.html", {"form": form})




# from django.shortcuts import render, get_object_or_404, redirect
# from .models import *
# from rest_framework import generics
# from django.contrib.auth.models import User
# from .serializers import UserSerializer
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from .forms import FilmForm
# from django.contrib.auth import login as auth_login
# from itertools import chain


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('films')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

# def login_view(request):
#     if request.user.is_authenticated:
#         return redirect('films')
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data=request.POST)
#         if form.is_valid():
#             user = form.get_user()
#             auth_login(request, user)
#             return redirect('films')  # asosiy sahifa
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def user_logout(request):
#     logout(request)
#     return redirect('films')

# def add_film_view(request):
#     if request.method == "POST":
#         form = FilmForm(request.POST, request.FILES)
#         if form.is_valid():
#             film = form.save(commit=False)

#             # Agar foydalanuvchi anonim tanlasa created_by = None
#             anonymous = request.POST.get("anonymous")  # checkbox qiymati
#             if anonymous:
#                 film.created_by = None
#             elif request.user.is_authenticated:
#                 film.created_by = request.user
#             else:
#                 film.created_by = None

#             film.approved = False
#             film.save()
#             form.save_m2m()
            
#             return redirect("films")
#     else:
#         form = FilmForm()

#     return render(request, "film_add.html", {"form": form})


# def register_view(request):
#     if request.user.is_authenticated:
#         return redirect('films')
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request, user)
#             return redirect('films')  # asosiy sahifa
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})



# def film_detail(request, pk):
#     film = get_object_or_404(Film,pk=pk)
#     actors = [a.strip() for a in film.actor.split(",")]
#     return render(request, "film_detail.html", {"film": film, "actors": actors})


# def film_category(request, pk):
#     janr = get_object_or_404(Janr, pk=pk)
#     films = Film.objects.filter(genres=janr)

#     return render(request, "film_category.html", {
#         "janr": janr,
#         "films": films,
#         "categories": Janr.objects.all()
#     })



# def films(request):
#     search = request.GET.get("search")
    
#     # Faqat approved=True bo'lgan filmlarni ko'rsatamiz
#     films = Film.objects.filter(approved=True)

#     if search:
#         films = films.filter(
#             name__icontains=search
#         )

#     return render(request, 'film.html', {
#         "films": films,
#         "categories": Janr.objects.all()
#     })


