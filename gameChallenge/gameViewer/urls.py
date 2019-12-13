from django.urls import url, path
from django.conf.urls.static import static
from . import views
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path(r'^add_game/$', views.addGame, name='add_game'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)