from django.shortcuts import render
from django.http import HttpResponse
from gameViewer.models import Game
from gameViewer.forms import GameForm


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def addGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST)

        # Check form is valid
        if form.is_valid():
            game= form.save(commit=False)
            return index(request)
        else:
            print(form.errors)

    form = GameForm()
    return render(request, 'gameViewer/add_game.html', {'form': form})


def viewGame(request):

    try:
        # Try finding the game from the slug
        game = Game.objects.get(slug=game_name_slug)

    # Reset if game was not found
    except Game.DoesNotExist:
        context_dict['game'] = None

    return render(request, 'gameviewer/game.html', context_dict)


