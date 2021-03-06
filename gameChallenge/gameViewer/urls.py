from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings
from django.conf.urls import url


urlpatterns = [
    path('', views.index, name='index'),
    url(r'^add_game/$', views.addGame, name='add_game'),
    url(r'^game/(?P<game_name_slug>[\w\-]+)/$', views.viewGame, name='view_game')
] 
