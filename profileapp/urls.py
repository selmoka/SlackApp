from django.urls import path, reverse

from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    path('profile', views.profile, name='profile'),
    path('addprofile', views.addprofile, name='addprofile'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
]