from django.conf.urls import url, include
from usersphones import views


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^update/(?P<id>\d+)$', views.update_movies),
    url(r'genesis-api/movies$', views.movies_api),
    url(r'genesis-api/performances$', views.performances_api),
    url(r'^movie/details/(?P<id>\d+)/(?P<movie_code>[\w]+)/$', views.movie_details, name='movie_details'),
    url(r'^movies/location/id/(?P<id>\d+)/$', views.movies_location, name='movie_location'),
    url(r'^book/movie/(?P<book_url>[\w]+)', views.book_movie, name='book_movie'),
    #url(r'^users/phone/save', include('usersphones.urls')),


    url(r'^api/$', views.UserCreateView.as_view(), name="user_create"),
    url(r'^api/list/$', views.user_list, name="users_list"),
    url(r'^api/(?P<pk>\d+)/detail/$', views.user_details, name="user_detail"),
    url(r'^api/(?P<pk>\d+)/update/$', views.user_update, name="user_update"),
    url(r'^api/(?P<pk>\d+)/delete/$', views.user_delete, name="user_delete"),
]