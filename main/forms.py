from django.forms import ModelForm
from main.models import Anime

class AnimeForm(ModelForm):
    class Meta:
        model = Anime
        fields = ["name", "episodes", "synopsis", "rating", "studio", "genre", "release_date"]