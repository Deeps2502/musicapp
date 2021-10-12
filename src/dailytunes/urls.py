from django.urls import path, include, re_path
from . import views as dailytunes_views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'dailytunes'
urlpatterns = [
    #home /
    path('', dailytunes_views.home, name='home'),

    #home1 /
    path('', dailytunes_views.home1, name='home1'),


    #about/
    path('about.html', dailytunes_views.about,name='about'),

    #profile_detail /@username/
    path('@<str:username>/', dailytunes_views.profile_detail, name='profile_detail'),

    #add new album /@username/add
    path('@<str:username>/add/', dailytunes_views.add_album, name='add_album'),

    #album's detail page /@username/album/album_name
    path('@<str:username>/album/<str:album>/', dailytunes_views.album_detail, name='album_detail'),

    # login the user /login/
    path('login/', LoginView.as_view(template_name='dailytunes/login.html'), name="login"),

    # signUp new user /signup/
    path('signup/', dailytunes_views.signup, name='signup'),

    #delete album /@username/album/album_name/delete
    path('@<str:username>/album/<str:album>/delete/', dailytunes_views.delete_album, name='delete_album'),

    #add songs to the albums
    path('@<str:username>/album/<str:album>/add/', dailytunes_views.add_song, name='add_song'),

    #logout the current user
    path('logout/', LogoutView.as_view(), name='logout'),
]
