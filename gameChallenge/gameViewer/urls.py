from django.urls import path
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path(r'^add_game/$', views.addGame, name='add_game'),
    path(r'^view_game/$', views.viewGame, name='view_game')
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)