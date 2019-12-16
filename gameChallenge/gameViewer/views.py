from django.shortcuts import render
from django.http import HttpResponse
from gameViewer.models import Game
from gameViewer.forms import GameForm


def index(request):
    context_dict = {
        "Games": Game.objects.all()
    }
    response = render(request, 'gameViewer/index.html', context_dict)
    return response

def addGame(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)

        # Check form is valid
        if form.is_valid():
            game= form.save(commit=False)
            print(request.POST)
            print(request.FILES)
            if 'picture' in request.FILES:
                game.picture = request.FILES['picture']
            game.save()
            return index(request)
        else:
            print(form.errors)

    form = GameForm()
    return render(request, 'gameViewer/add_game.html', {'form': form})


def viewGame(request, game_name_slug):

    context_dict = {}

    try:
        # Try finding the game from the slug
        game = Game.objects.get(slug=game_name_slug)
        context_dict['game'] = game

    # Reset if game was not found
    except Game.DoesNotExist:
        context_dict['game'] = None

    return render(request, 'gameViewer/game.html', context_dict)

