from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import SpaceRoom
from .forms import SpaceRoomForm
from django.contrib import messages


# @login_required
def mapCreate(request) :
    return render(request, 'mapCreate.html')


# --------------- CLASSROOM (CREATE) ---------------
# @login_required
def Classroom_Create(request) :
    if request.method == 'POST':

        form = SpaceRoomForm(request.POST)
        if form.is_valid():

            form.save()

        else :
            messages.info(request, "Space Name cannot be blank.")

    Classrooms = {'SpaceRoom':SpaceRoom}
    return render(request, 'classroom_create.html', Classrooms)

# --------------- FOREST (CREATE) ---------------
# @login_required
def Forest_Create(request) :
    if request.method == 'POST':

        form = SpaceRoomForm(request.POST)
        if form.is_valid():

            form.save()

        else :
            messages.info(request, "Space Name cannot be blank.")

    Classrooms = {'SpaceRoom':SpaceRoom}
    return render(request, 'forest_create.html', Classrooms)

# --------------- CAFE (CREATE) ---------------
# @login_required
def Cafe_Create(request) :
    if request.method == 'POST':

        form = SpaceRoomForm(request.POST)
        if form.is_valid():

            form.save()

        else :
            messages.info(request, "Space Name cannot be blank.")

    Classrooms = {'SpaceRoom':SpaceRoom}
    return render(request, 'cafe_create.html', Classrooms)

# --------------- LIBRARY (CREATE) ---------------
# @login_required
def Library_Create(request) :
    if request.method == 'POST':

        form = SpaceRoomForm(request.POST)
        if form.is_valid():

            form.save()

        else :
            messages.info(request, "Space Name cannot be blank.")

    Classrooms = {'SpaceRoom':SpaceRoom}
    return render(request, 'library_create.html', Classrooms)

# --------------- BEACH (CREATE) ---------------
# @login_required
def Beach_Create(request) :
    if request.method == 'POST':

        form = SpaceRoomForm(request.POST)
        if form.is_valid():

            form.save()

        else :
            messages.info(request, "Space Name cannot be blank.")

    Classrooms = {'SpaceRoom':SpaceRoom}
    return render(request, 'beach_create.html', Classrooms)




# --------------- CLASSROOM (JOIN) ---------------
# @login_required
def Classroom_Rooms(request):
    rooms = SpaceRoom.objects.all()

    return render(request, 'classroom_rooms.html', {'rooms':rooms})

# @login_required
def Room(request, roomName):
    room = SpaceRoom.objects.get(roomName=roomName)

    return render(request, 'room.html', {'room':room})

# --------------- FOREST (JOIN) ---------------
# @login_required
def Forest_Rooms(request):
    rooms = SpaceRoom.objects.all()

    return render(request, 'forest_rooms.html', {'rooms':rooms})

# --------------- CAFE (JOIN) ---------------
# @login_required
def Cafe_Rooms(request):
    rooms = SpaceRoom.objects.all()

    return render(request, 'cafe_rooms.html', {'rooms':rooms})

# --------------- LIBRARY (JOIN) ---------------
# @login_required
def Library_Rooms(request):
    rooms = SpaceRoom.objects.all()

    return render(request, 'library_rooms.html', {'rooms':rooms})

# --------------- BEACH (JOIN) ---------------
# @login_required
def Beach_Rooms(request):
    rooms = SpaceRoom.objects.all()

    return render(request, 'beach_rooms.html', {'rooms':rooms})