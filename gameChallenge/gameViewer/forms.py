from django import forms
from gameViewer.models import Game

#Form to add a game
class GameForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           help_text="Name of Game")
    platform = forms.CharField(max_length=50,
                            help_text="Platform")
    genre = forms.CharField(max_length=50,
                            help_text="Genre")
    release_date = forms.DateField(help_text = "Release Date")
    publisher = forms.CharField(max_length=50,
                            help_text="Publisher")
    n_players = forms.IntegerField(help_text = "Number of Players")
    picture = forms.ImageField(required=False)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)


    class Meta:
        model = Game
        fields = ('name','platform','genre', 'release_date','publisher', 'n_players', 'picture')