from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'movie/(?P<movie_name>[A-z .0-9()]+)/$', views.movie, name='movie'),
]
