from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import AnimeForm
from main.models import Anime
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    allAnime = Anime.objects.filter(user=request.user)
    context = {
        'name': request.user.username,
        'class': 'PBP A',
        'allAnime': allAnime,
         'last_login': request.COOKIES['last_login']
        
    }

    return render(request, "main.html", context)

def create_anime(request):
    form = AnimeForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
     anime = form.save(commit=False)
     anime.user = request.user
     anime.save()
     return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_anime.html", context)

@csrf_exempt
def add_anime_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        episodes = request.POST.get("episodes")
        synopsis = request.POST.get("synopsis")
        rating = request.POST.get("rating")
        studio = request.POST.get("studio")
        genre = request.POST.get("genre")
        release_date = request.POST.get("release_date")
        user = request.user

        new_anime = Anime(name=name, episodes=episodes, synopsis=synopsis, rating=rating, studio=studio, genre=genre, release_date=release_date, user=user)
        new_anime.save()
        return HttpResponse(b"CREATED", status=201)
    return HttpResponseNotFound()
    


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_anime(request, id):
    
    anime = Anime.objects.get(pk = id)

    form = AnimeForm(request.POST or None, instance=anime)

    if form.is_valid() and request.method == "POST":
    
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_anime.html", context)

def delete_anime(request, id):
    anime = Anime.objects.get(pk = id)
    anime.delete()
    return HttpResponseRedirect(reverse('main:show_main'))


def show_xml(request):
    data = Anime.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Anime.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Anime.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Anime.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

