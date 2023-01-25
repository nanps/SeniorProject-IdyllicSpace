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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),

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
]