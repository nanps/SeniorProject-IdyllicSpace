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

    path('create', views.mapCreate, name='create'),
    
    path('createClassroom', views.Classroom_Create, name='createClassroom'),
    path('createForest', views.Forest_Create, name='createForest'),
    path('createCafe', views.Cafe_Create, name='createCafe'),
    path('createLibrary', views.Library_Create, name='createLibrary'),
    path('createBeach', views.Beach_Create, name='createBeach'),

    path('classroom', views.Classroom_Rooms, name='classroom_rooms'),
    path('forest', views.Forest_Rooms, name='forest_rooms'),
    path('cafe', views.Cafe_Rooms, name='cafe_rooms'),
    path('library', views.Library_Rooms, name='library_rooms'),
    path('beach', views.Beach_Rooms, name='beach_rooms'),

    path('space/', views.space, name='space'),

    path('Classroom/<slug:slug>/', views.Classroom_Space, name='classroomSpace'),
    path('Forest/<slug:slug>/', views.Forest_Space, name='forestSpace'),
    path('Cafe/<slug:slug>/', views.Cafe_Space, name='cafeSpace'),
    path('Library/<slug:slug>/', views.Library_Space, name='librarySpace'),
    path('Beach/<slug:slug>/', views.Beach_Space, name='beachSpace'),
]