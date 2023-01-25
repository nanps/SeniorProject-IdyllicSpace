from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('home/', views.home, name='home'),
    path('enterDisplayName/', views.enterDisplayName, name='enterDisplayName'),

    path('maleAvatar/', views.maleAvatar, name='maleAvatar'),
    path('femaleAvatar/', views.femaleAvatar, name='femaleAvatar'),
    path('mysteryAvatar/', views.mysteryAvatar, name='mysteryAvatar'),

    path('space/', views.space, name='space'),
]