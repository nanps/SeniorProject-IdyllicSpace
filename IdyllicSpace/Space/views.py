from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SpaceRoom, UserManage
from django.contrib.auth.models import User
from .forms import SpaceRoomForm, DisplayNameForm, AvatarForm
from django.contrib import messages


# Create your views here.
def home(request) :   

    usernameInput = request.user 

    if request.method == 'POST':

        if (UserManage.objects.filter(username=usernameInput).exists()) :
            return render(request, 'statusLogIn.html')
        else :
            return redirect('maleAvatar')

    return render(request, 'home.html')


def space(request) :
    usernameInput = request.user

    userData = UserManage.objects.get(username=usernameInput)
    user = User.objects.get(username=usernameInput)

    return render(request, 'space.html', {'userData':userData,'user':user} )


def enterDisplayName(request) :

    usernameInput = request.user

    if request.method == 'POST':
        
        form = DisplayNameForm(request.POST)

        if form.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():

                instance = form.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['displayName'])

                return render(request, 'statusLogIn.html') #อย่าลืมแก้
            else :
                instance = form.save(commit=False)
                instance.username = request.user
                instance.save()

                return render(request, 'statusLogIn.html') #อย่าลืมแก้
        else :
            messages.info(request, "Display Name cannot be blank.")


    return render(request, 'enterDisplayName.html')


def maleAvatar(request) :

    usernameInput = request.user

    if request.method == 'POST':
        
        form = AvatarForm(request.POST)

        if form.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():

                instance = form.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['avatar'])

                return redirect('enterDisplayName')
            else :
                instance = form.save(commit=False)
                instance.username = request.user
                instance.save()

                return redirect('enterDisplayName')
        else :
            messages.info(request, "You must choose one Avatar.")

    else:
        form = AvatarForm()

    return render(request, 'maleAvatar.html')


def femaleAvatar(request) :
    
    usernameInput = request.user

    if request.method == 'POST':
        
        form = AvatarForm(request.POST)

        if form.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():

                instance = form.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['avatar'])

                return redirect('enterDisplayName')
            else :
                instance = form.save(commit=False)
                instance.username = request.user
                instance.save()

                return redirect('enterDisplayName')
        else :
            messages.info(request, "You must choose one Avatar.")

    else:
        form = AvatarForm()

    return render(request, 'femaleAvatar.html')


def mysteryAvatar(request) :
        
    usernameInput = request.user

    if request.method == 'POST':
        
        form = AvatarForm(request.POST)

        if form.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():

                instance = form.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['avatar'])

                return redirect('enterDisplayName')
            else :
                instance = form.save(commit=False)
                instance.username = request.user
                instance.save()

                return redirect('enterDisplayName')
        else :
            messages.info(request, "You must choose one Avatar.")

    else:
        form = AvatarForm()

    return render(request, 'mysteryAvatar.html')


# map
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