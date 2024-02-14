from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import AnimeForm
from main.models import Anime

# Create your views here.
def show_main(request):
    allAnime = Anime.objects.all()
    context = {
        'name': 'Muhammad Eagel Triutama',
        'class': 'PBP A',
        'allAnime': allAnime
        
    }

    return render(request, "main.html", context)

def create_anime(request):
    form = AnimeForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_anime.html", context)

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

