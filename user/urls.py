from django.urls import path
from . import views

app_name = 'user'

urlpatterns=[
    path('signin/',views.SigninView,name='signin'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('profile/',views.ProfileView,name='profile'),
    path('signout/',views.SignoutView,name='signout'),
]
