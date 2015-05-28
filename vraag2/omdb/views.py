from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader
from django.views import generic

import redis
import json
import urllib2
# Create your views here.
r = redis.StrictRedis(host='localhost', port=6379, db=0)

def fill_db():

    r.set('movie:1', "The Hobbit")
    r.set('movie:1:1', '{"Title":"The Hobbit","Year":"1977","Rated":"NOT RATED","Released":"27 Nov 1977","Runtime":"90 min","Genre":"Animation, Adventure, Family","Director":"Jules Bass, Arthur Rankin Jr.","Writer":"J.R.R. Tolkien (novel), Romeo Muller","Actors":"Orson Bean, Richard Boone, Hans Conried, John Huston","Plot":"A homebody hobbit in Middle Earth gets talked into joining a quest with a group of dwarves to recover their treasure from a dragon.","Language":"English","Country":"USA","Awards":"1 win & 2 nominations.","Poster":"http://ia.media-imdb.com/images/M/MV5BMjA0ODY3NTkwOF5BMl5BanBnXkFtZTcwODU3NzIyMQ@@._V1_SX300.jpg","Metascore":"N/A","imdbRating":"6.7","imdbVotes":"9135","imdbID":"tt0077687","Type":"movie","Response":"True"}' )
fill_db()

def movie(request, movie_name):
    movie_keys = r.keys('movie:*')
    movie = {}
    for m in movie_keys:
        movie_t = json.loads(r.get(m))
    	if movie_t['Title'] == movie_name:
            movie = movie_t
            movie_id = m.split(':')[1]
        else:
            response = urllib2.urlopen("http://www.omdbapi.com/?t=movie_name")
            #data = json.load(response)
            print response


    return render(request, 'omdb/movie.html', {'movie': movie})
