from django import forms
from gameViewer.models import Game

#Form to add a game
class GameForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           help_text="name of game.")
    platform = forms.CharField(max_length=50,
                            help_text="platform.")
    genre = forms.CharField(max_length=50,
                            help_text="genre.")
    release_date = forms.DateField(help_text = "release date")
    publisher = forms.CharField(max_length=50,
                            help_text="publisher.")
    n_players = forms.IntegerField(help_text = "number of players")

    slug = forms.CharField(widget=forms.HiddenInput(), required=False)


    class Meta:
        model = Game
        fields = ('name','platform','genre', 'release_date','publisher', 'n_players')