from django.contrib import admin
from models import UsersPhone, Movies, MoviesPerformances, Location, MoviesFullDetails
# Register your models here.


class UsersPhoneAdmin(admin.ModelAdmin):
    list_display = [field.name for field in UsersPhone._meta.fields if field.name != "id"]
    search_fields = ('phone',)
    list_filter = ("phone",)


class MoviesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Movies._meta.fields if field.name != "id"]
    search_fields = ('movie_code', 'movie_title', )
    list_filter = ("movie_start_date", "movie_genre", )

class MoviesFullDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MoviesFullDetails._meta.fields if field.name != "id"]
    search_fields = ('movie_code', 'movie_title', )
    list_filter = ("movie_start_date", "movie_genre", )

class MoviesPerformancesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MoviesPerformances._meta.fields if field.name != "id"]
    search_fields = ('booking_url', 'film_code', )
    list_filter = ("start_time", "perform_date", )

admin.site.register(UsersPhone, UsersPhoneAdmin)
admin.site.register(Movies, MoviesAdmin)
admin.site.register(MoviesFullDetails, MoviesFullDetailsAdmin)
admin.site.register(Location)
admin.site.register(MoviesPerformances, MoviesPerformancesAdmin)
