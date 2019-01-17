from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UsersPhone(models.Model):
    phone = models.CharField(max_length=11, default="")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone

    class Meta:
        verbose_name_plural = "Users Phone Numbers"


class Location(models.Model):
    location = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.location


class Movies(models.Model):
    movie_title = models.CharField(max_length=250, default="")
    movie_code = models.CharField(max_length=20, default="")
    movie_running_time = models.CharField(max_length=500, default="")
    movie_synopsis = models.CharField(max_length=500, default="", null=True, blank=True)
    movie_genre = models.CharField(max_length=20, default="")
    movie_start_date = models.CharField(max_length=200, default="")
    movie_thumbnail = models.CharField(max_length=200, default="")
    movie_certificate = models.CharField(max_length=200, default="")
    movie_banner = models.ImageField(default="", upload_to = "static/images/banners",null=True, blank=True )
    movie_location = models.CharField(max_length=250, default="")
    movie_featured = models.BooleanField(default=False)
    movie_popular = models.BooleanField(default=False)
    movie_pop_thumbnail = models.ImageField(default="", upload_to = "static/images/popular_thumbnails",null=True, blank=True )

    def __str__(self):
        return self.movie_title
    class Meta:
        verbose_name_plural = "All Movies"
        unique_together = ('movie_code', 'movie_location')

class MoviesPerformances(models.Model):
    film_code = models.CharField(max_length=500, default="")
    start_time = models.CharField(max_length=200, default="")
    perform_date = models.CharField(max_length=500, default="")
    booking_url = models.CharField(max_length=20, default="")
    movie_location = models.CharField(max_length=250, default="")
    movie_start_date = models.CharField(max_length=200, default="")

    def __str__(self):
        return self.film_code
    class Meta:
        verbose_name_plural = "All Perfomances"

class MoviesFullDetails(models.Model):
    movie_title = models.CharField(max_length=250, default="")
    movie_code = models.CharField(max_length=20, default="")
    movie_running_time = models.CharField(max_length=500, default="")
    movie_synopsis = models.CharField(max_length=500, default="")
    movie_genre = models.CharField(max_length=20, default="")
    movie_start_date = models.CharField(max_length=200, default="")
    movie_thumbnail = models.CharField(max_length=200, default="")
    movie_certificate = models.CharField(max_length=200, default="")
    film_code = models.CharField(max_length=500, default="")
    start_time = models.CharField(max_length=200, default="")
    perform_date = models.CharField(max_length=500, default="")
    booking_url = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.movie_title
    class Meta:
        verbose_name_plural = "Full Movies Details"

