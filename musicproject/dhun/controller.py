from django.urls import path
from . import views
app_name='dhun'
urlpatterns = [
    path("",views.home,name='home'),
    path("songs/<int:pk>",views.detail,name='song'),
    path("user/signup",views.signup,name='signup'),
    path("user/signin",views.signin,name='signin'),
    path("user/signout",views.signout,name='signout'),
    path("user/album/create",views.Add_Album.as_view(),name='addalbum'),
    path("user/album/<int:pk>",views.Upalbum.as_view(),name='upalbum'),
    path("user/album/del/<int:pk>",views.Delalbum.as_view(),name='delalbum'),
    path("user/song/add/<int:pk>",views.Add_song.as_view(),name='addsong'),
    path("user/song/update/<int:pk>",views.Upsong.as_view(),name='upsong'),
    path("user/song/delete/<int:pk>",views.Delsong.as_view(),name='delsong'),
    path("home",views.Myhome.as_view(),name='loghome'),
    path("user/Profile/create",views.addProfile.as_view(),name='addprofile'),
    path("upprofile",views.Uprofile.as_view(),name='upprofile'),
    path("user/profile/update/<int:pk>",views.UPProfile.as_view(),name='editprofile'),
    path('search', views.search, name='search')
    ]