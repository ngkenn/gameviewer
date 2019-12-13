from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def addGame(request):
     form = GameForm()
    if request.method == 'POST':
        form = GameForm(request.POST)

        # Check form is valid
        if form.is_valid():
            game= form.save(commit=False)
            return index(request)
        else:
            print(form.errors)


    return render(request, 'gameViewer/add_game.html')



def viewGame():


