"""IdyllicSpace URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('logOut/', auth_views.LogoutView.as_view(), name='logOut'),

    path('', auth_views.LoginView.as_view(template_name='logIn.html'), name='logIn'),

    path('home/', include('Space.urls')), # /home/home

    path('createAcc/', views.createAcc, name='createAcc'),
    path('signUpSuccess/', views.signUpSuccess, name='signUpSuccess'),

    path('forgotPassEmail/', views.forgotPassEmail, name='forgotPassEmail'),
    path('forgotPassPassword/', views.forgotPassPassword, name='forgotPassPassword'),
    path('checkEmailPage/', views.checkEmailPage, name='checkEmailPage'),
    path('resetPassSuccess/', views.resetPassSuccess, name='resetPassSuccess'),

    path('Space/', include('Space.urls')), 
        # /Space/enterDisplayName
        # /Space/maleAvatar
        # /Space/femaleAvatar
        # /Space/mysteryAvatar
        # /Space/space

        # /Space/Classroom/<slug:slug>/      url for open Space Room
        # /Space/Forest/<slug:slug>/ 
        # /Space/Cafe/<slug:slug>/ 
        # /Space/Library/<slug:slug>/ 
        # /Space/Beach/<slug:slug>/ 

    path('enterCode/', views.enterCode, name='enterCode'),
    path('enterSpace/', views.enterSpace, name='enterSpace'),
    path('statusLogIn/', views.statusLogIn, name='statusLogIn'),

    path('mapJoin/', views.mapJoin, name='mapJoin'),
    path('mapCreate/', include('Space.urls')), # /mapCreate/create

    path('classroom_create/', include('Space.urls')), # /classroom_create/createClassroom
    path('forest_create/', include('Space.urls')), # /forest_create/createForest
    path('cafe_create/', include('Space.urls')), # /cafe_create/createCafe
    path('library_create/', include('Space.urls')), # /library_create/createLibrary
    path('beach_create/', include('Space.urls')), # /beach_create/createBeach

    path('classroom_rooms/', include('Space.urls')), # /classroom_rooms/classroom
    path('forest_rooms/', include('Space.urls')), # /forest_rooms/forest
    path('cafe_rooms/', include('Space.urls')), # /cafe_rooms/cafe
    path('library_rooms/', include('Space.urls')), # /library_rooms/library
    path('beach_rooms/', include('Space.urls')), # /beach_rooms/beach
]