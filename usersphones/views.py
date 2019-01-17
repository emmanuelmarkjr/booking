# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import UsersPhone, MoviesPerformances, Movies, Location
from .serializers import UsersPhoneSerializer, MoviesPerformancesSerializer, MoviesSerializer
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from xml.dom import minidom
#import os
import urllib
import datetime
from dateutil import parser
from usersphones.models import Movies, MoviesPerformances, MoviesFullDetails
from django.http import HttpResponse
from django.db.models import Q
from datetime import timedelta
import re


def week_range(date):
    year, week, dow = date.isocalendar()
    if dow == 7:
        start_date = date
    else:
        start_date = date - timedelta(dow)
    end_date = start_date + timedelta(6)

    return (start_date, end_date)

now = datetime.datetime.now()
today_date = now.strftime("%Y-%m-%d")

#from moviesAPI.settings import BASE_DIR



def update_movies(request, id):
    url_str = 'http://roemeo.com/xml/pfapache.py?type=MEDIA2&sitekey=3BFXv06X6285GeuG'
    if id == 1:
        url_str = 'http://roemeo.com/xml/pfapache.py?type=MEDIA2&sitekey=3BFXv06X6285GeuG'
    elif id == 2:
        url_str = 'http://roemeo.com/xml/pfapache.py?type=MEDIA2&sitekey=xjNHSrz6pOfqsGc9'
    elif id == 3:
        url_str = 'http://roemeo.com/xml/pfapache.py?type=MEDIA2&sitekey=nW91FyMwlG0gOKNc'
    elif id == 4:
        url_str = 'http://roemeo.com/xml/pfapache.py?type=MEDIA2&sitekey=B7jvtzefATRl3PKX'
    elif id == 5:
        url_str = 'http://roemeo.com/xml/pfapache.py?type=MEDIA2&sitekey=vX7sc2kv9GDpb9Ww'
    elif id == 6:
        url_str = 'http://roemeo.com/xml/pfapache.py?type=MEDIA2&sitekey=JOu2v5pC9LUah8GI'
    elif id == 7:
        url_str = 'http://roemeo.com/xml/pfapache.py?type=MEDIA2&sitekey=Y55MM0y0jmhtJPBx'
    xml_str = urllib.urlopen(url_str).read()
    movie_xml = minidom.parseString(xml_str)
    Films = movie_xml.getElementsByTagName("Film")
    Performances = movie_xml.getElementsByTagName("Performance")
    for Film in Films :
        movie_title = Film.getElementsByTagName("FilmTitle")[0].firstChild.data
        movie_code = Film.getElementsByTagName("Code")[0].firstChild.data
        movie_running_time = Film.getElementsByTagName("RunningTime")[0].firstChild.data
        try:
            movie_synopsis = Film.getElementsByTagName("Synopsis")[0].firstChild.data
        except AttributeError:
            movie_synopsis = Film.getElementsByTagName("Synopsis")[0].firstChild
        movie_genre = Film.getElementsByTagName("Genre")[0].firstChild.data
        movie_start_date = Film.getElementsByTagName("StartDate")[0].firstChild.data
        movie_thumbnail = Film.getElementsByTagName("Img_1s")[0].firstChild.data
        movie_certificate = Film.getElementsByTagName("Certificate")[0].firstChild.data
        Movies.objects.update_or_create(

                movie_code=movie_code,movie_title=movie_title,movie_synopsis=movie_synopsis,movie_location=id,movie_running_time=movie_running_time,movie_genre=movie_genre,movie_start_date=movie_start_date,movie_thumbnail=movie_thumbnail,movie_certificate=movie_certificate
        )
    for Performance in Performances :
        film_code = Performance.getElementsByTagName("FilmCode")[0].firstChild.data
        start_time = Performance.getElementsByTagName("StartTime")[0].firstChild.data
        d = datetime.datetime.strptime(start_time, "%H:%M:%S")
        start_time = d.strftime("%I:%M %p")
        perform_date = Performance.getElementsByTagName("PerformDate")[0].firstChild.data
        perform_date = parser.parse(perform_date).strftime("%a")
        booking_url = Performance.getElementsByTagName("BookingURL")[0].firstChild.data
        MoviesPerformances.objects.update_or_create(
                movie_start_date=movie_start_date,movie_location=id,film_code=film_code,start_time=start_time,perform_date=perform_date,booking_url=booking_url[-6:]
        )
    return HttpResponse("Movies Successfully Updated")

def home(request):
    locations = Location.objects.all()
    slider_movies = Movies.objects.filter(~Q(movie_synopsis=None), ~Q(movie_banner=None),movie_location=1)[:5]
    below_slider_movies = Movies.objects.filter(~Q(movie_thumbnail="None"))[:15]
    featured_movies = Movies.objects.filter(~Q(movie_thumbnail="None"), movie_featured=True)[:12]
    popular_movies = Movies.objects.filter(~Q(movie_thumbnail="None"),~Q(movie_synopsis=None), movie_popular=True)[:7]
    return render(request, 'userphones/index.html', {'locations': locations, 'slider_movies': slider_movies, 'below_slider_movies': below_slider_movies, 'featured_movies': featured_movies, 'popular_movies': popular_movies})


def movies_location(request, id):
    locations = Location.objects.all()
    slider_movies = Movies.objects.filter(~Q(movie_synopsis=None), ~Q(movie_banner=None),movie_location=1)[:5]
    below_slider_movies = Movies.objects.filter(~Q(movie_thumbnail="None"), movie_location=id)[:15]
    featured_movies = Movies.objects.filter(~Q(movie_thumbnail="None"), movie_location=id, movie_featured=True)[:12]
    popular_movies = Movies.objects.filter(~Q(movie_thumbnail="None"),~Q(movie_synopsis=None), movie_location=id, movie_popular=True)[:7]
    return render(request, 'userphones/index.html', {'location_name': id, 'locations': locations, 'slider_movies': slider_movies, 'below_slider_movies': below_slider_movies, 'featured_movies': featured_movies, 'popular_movies': popular_movies})


def movie_details(request, id, movie_code):
    below_slider_movies = Movies.objects.filter(~Q(movie_thumbnail="None"), movie_location=id)[:15]
    next_movies = Movies.objects.filter(~Q(movie_thumbnail="None"))[:8]
    movies_detail = Movies.objects.filter(movie_code=movie_code)[:1]
    movies_detail_performance = MoviesPerformances.objects.filter(film_code=movie_code, movie_location=id)
    return render(request, 'userphones/movie_details.html', {'movies_detail_performance': movies_detail_performance, 'movies_detail': movies_detail, 'next_movies': next_movies, 'below_slider_movies': below_slider_movies})


def book_movie(request, book_url):
    locations = Location.objects.all()
    url = "https://www.jack-roe.co.uk/TaposWebSales/Main/GENLAG/book?perfcode=" + book_url
    return render(request, 'book_movie.html', {'book_url': url, 'locations': locations})





###### API views.    ######

class UserCreateView(generics.CreateAPIView):
    serializer_class = UsersPhoneSerializer


@api_view(["GET"])
def user_details(request, pk):
    user = UsersPhone.objects.get(id=pk)
    serializer = UsersPhoneSerializer(user)
    return Response(serializer.data)


@api_view(["GET", "PUT"])
def user_update(request, pk):
    user = UsersPhone.objects.get(id=pk)
    if request.method == "PUT":
        serializer = UsersPhoneSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": serializer.errors, "error": True})
    serializer = UsersPhoneSerializer(user)
    return Response(serializer.data)


@api_view(["GET"])
def user_list(request):
    users = UsersPhone.objects.all()
    serializer = UsersPhoneSerializer(users, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def movies_api(request):
    movies = Movies.objects.all()
    serializer = MoviesSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def performances_api(request):
    performances = MoviesPerformances.objects.all()
    serializer = MoviesPerformancesSerializer(performances, many=True)
    return Response(serializer.data)


def user_delete(request, pk):
    user = get_object_or_404(UsersPhone, id=pk)
    user.delete()
    return Response({"message": "Deleted"})