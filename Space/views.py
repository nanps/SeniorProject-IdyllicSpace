from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SpaceRoom, UserManage, ChatMessage
from django.contrib.auth.models import User
from .forms import SpaceRoomForm, DisplayNameForm, AvatarForm, BioForm, CurrentSpaceRoomForm, MessageForm, MoodForm
from django.contrib import messages


# Create your views here.
def home(request) :   

    usernameInput = request.user 

    if request.method == 'POST':

        if (UserManage.objects.filter(username=usernameInput).exists()) :
            return redirect('enterSpace')
        else :
            return redirect('maleAvatar')

    return render(request, 'home.html')


def enterDisplayName(request) :

    usernameInput = request.user

    if request.method == 'POST':
        
        form = DisplayNameForm(request.POST)

        if form.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():

                instance = form.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['displayName'])

                return redirect('enterSpace')
            else :
                instance = form.save(commit=False)
                instance.username = request.user
                instance.save()

                return redirect('enterSpace')
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

#Edit Avatar
def maleAvatarEdit(request) :
    usernameInput = request.user
    if request.method == 'POST':
        form = AvatarForm(request.POST)
        if form.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = form.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['avatar'])

                return redirect('editAvatarSuccess')
        else :
            messages.info(request, "You must choose one Avatar.")
    else:
        form = AvatarForm()

    return render(request, 'maleAvatar_edit.html')


def femaleAvatarEdit(request) :
    usernameInput = request.user
    if request.method == 'POST':
        form = AvatarForm(request.POST)
        if form.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = form.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['avatar'])

                return redirect('editAvatarSuccess')
        else :
            messages.info(request, "You must choose one Avatar.")
    else:
        form = AvatarForm()

    return render(request, 'femaleAvatar_edit.html')


def mysteryAvatarEdit(request) :
    usernameInput = request.user
    if request.method == 'POST':
        form = AvatarForm(request.POST)
        if form.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():

                instance = form.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['avatar'])

                return redirect('editAvatarSuccess')
        else :
            messages.info(request, "You must choose one Avatar.")
    else:
        form = AvatarForm()

    return render(request, 'mysteryAvatar_edit.html')

def editAvatarSuccess(request) :
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    return render(request, 'editAvatarSuccess.html', {'userData':userData})

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
            return redirect('classroom_rooms')

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
            return redirect('forest_rooms')

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
            return redirect('cafe_rooms')

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
            return redirect('library_rooms')

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

            # slugNEW = request.POST['slug']
            # capacityNEW = request.POST['capacity']
            # inRoomNEW = 0
            # roomStatusNEW = "open"

            # newRoom = Models.objects.create(slug=slugNEW, capacity=capacityNEW, inRoom=inRoomNEW, roomStatus=roomStatusNEW)
            # newRoom.save()

            form.save()
            return redirect('beach_rooms')

        else :
            messages.info(request, "Space Name cannot be blank.")

    Classrooms = {'SpaceRoom':SpaceRoom}
    return render(request, 'beach_create.html', Classrooms)





# --------------- CLASSROOM (JOIN) ---------------
# @login_required
def Classroom_Rooms(request):
    rooms = SpaceRoom.objects.all()

    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    usernameInput = request.user
    if request.method == 'POST':
        CSRform = CurrentSpaceRoomForm(request.POST)
        if CSRform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = CSRform.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['currentSpaceRoom'])
            return redirect('classroomConfirm')

    return render(request, 'classroom_rooms.html', {'rooms':rooms, 'userData':userData,})

def Classroom_Confirm(request):
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    rooms = SpaceRoom.objects.all()
    for room in rooms :
        if room.slug in userData.currentSpaceRoom :
            room.inRoom += 1
            room.save()

    return render(request, 'classroom_rooms_confirm.html', {'rooms':rooms, 'userData':userData, })

# @login_required
def Room(request, roomName):
    room = SpaceRoom.objects.get(roomName=roomName)

    return render(request, 'room.html', {'room':room})

# --------------- FOREST (JOIN) ---------------
# @login_required
def Forest_Rooms(request):
    rooms = SpaceRoom.objects.all()

    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    usernameInput = request.user
    if request.method == 'POST':
        CSRform = CurrentSpaceRoomForm(request.POST)
        if CSRform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = CSRform.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['currentSpaceRoom'])
            return redirect('forestConfirm')

    return render(request, 'forest_rooms.html', {'rooms':rooms, 'userData':userData,})

def Forest_Confirm(request):
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    rooms = SpaceRoom.objects.all()
    for room in rooms :
        if room.slug in userData.currentSpaceRoom :
            room.inRoom += 1
            room.save()

    return render(request, 'forest_rooms_confirm.html', {'rooms':rooms, 'userData':userData, })

# --------------- CAFE (JOIN) ---------------
# @login_required
def Cafe_Rooms(request):
    rooms = SpaceRoom.objects.all()

    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    usernameInput = request.user
    if request.method == 'POST':
        CSRform = CurrentSpaceRoomForm(request.POST)
        if CSRform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = CSRform.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['currentSpaceRoom'])
            return redirect('cafeConfirm')

    return render(request, 'cafe_rooms.html', {'rooms':rooms, 'userData':userData, })

def Cafe_Confirm(request):
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    rooms = SpaceRoom.objects.all()
    for room in rooms :
        if room.slug in userData.currentSpaceRoom :
            room.inRoom += 1
            room.save()

    return render(request, 'cafe_rooms_confirm.html', {'rooms':rooms, 'userData':userData, })

# --------------- LIBRARY (JOIN) ---------------
# @login_required
def Library_Rooms(request):
    rooms = SpaceRoom.objects.all()

    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    usernameInput = request.user
    if request.method == 'POST':
        CSRform = CurrentSpaceRoomForm(request.POST)
        if CSRform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = CSRform.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['currentSpaceRoom'])
            return redirect('libraryConfirm')

    return render(request, 'library_rooms.html', {'rooms':rooms, 'userData':userData, })

def Library_Confirm(request):
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    rooms = SpaceRoom.objects.all()
    for room in rooms :
        if room.slug in userData.currentSpaceRoom :
            room.inRoom += 1
            room.save()

    return render(request, 'library_rooms_confirm.html', {'rooms':rooms, 'userData':userData, })

# --------------- BEACH (JOIN) ---------------
# @login_required
def Beach_Rooms(request):
    rooms = SpaceRoom.objects.all()

    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    usernameInput = request.user
    if request.method == 'POST':
        CSRform = CurrentSpaceRoomForm(request.POST)
        if CSRform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = CSRform.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['currentSpaceRoom'])
            return redirect('beachConfirm')

    return render(request, 'beach_rooms.html', {'rooms':rooms, 'userData':userData, })

def Beach_Confirm(request):
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    rooms = SpaceRoom.objects.all()
    for room in rooms :
        if room.slug in userData.currentSpaceRoom :
            room.inRoom += 1
            room.save()

    return render(request, 'beach_rooms_confirm.html', {'rooms':rooms, 'userData':userData, })




# --------------- CLASSROOM (SPACE) ---------------
# @login_required
def Classroom_Space(request, slug):
    room = SpaceRoom.objects.get(slug=slug)

    return render(request, 'classroom_space.html', {'room': room})

# --------------- FOREST (SPACE) ---------------
# @login_required
def Forest_Space(request, slug):
    room = SpaceRoom.objects.get(slug=slug)

    return render(request, 'forest_space.html', {'room': room})

# --------------- CAFE (SPACE) ---------------
# @login_required
def Cafe_Space(request, slug):
    room = SpaceRoom.objects.get(slug=slug)

    return render(request, 'cafe_space.html', {'room': room})

# --------------- LIBRARY (SPACE) ---------------
# @login_required
def Library_Space(request, slug):
    room = SpaceRoom.objects.get(slug=slug)

    return render(request, 'library_space.html', {'room': room})

# --------------- BEACH (SPACE) ---------------
# @login_required
def Beach_Space(request, slug):
    room = SpaceRoom.objects.get(slug=slug)
    
    ChatMessages = ChatMessage.objects.all

    usernameInput = request.user

    userData = UserManage.objects.get(username=usernameInput)
    user = User.objects.get(username=usernameInput)

    currSpaceValue = "Space/Beach/" + slug
    members = UserManage.objects.filter(currentSpaceRoom=currSpaceValue)

    if request.method == 'POST':
        DNform = DisplayNameForm(request.POST)
        if DNform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = DNform.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['displayName'])

                return render(request, 'beach_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, })
        # else :
        #     messages.info(request, "Display Name cannot be blank.")

        BIOform = BioForm(request.POST)
        if BIOform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instanceBio = BIOform.save(commit=False)
                instanceBio.username = request.user
                instanceBio.save(update_fields=['bio'])

                return render(request, 'beach_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })

        moodForm = MoodForm(request.POST)
        if moodForm.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instanceMood = moodForm.save(commit=False)
                instanceMood.username = request.user
                instanceMood.save(update_fields=['mood'])

                return render(request, 'beach_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })

        chatForm = MessageForm(request.POST)
        if chatForm.is_valid() :
            chatForm.instance.displayName = userData
            chatForm.save()

            #ทำให้ทุกเครื่องที่เข้าเว็บอยู่รีโหลดทั้งหมด

    return render(request, 'beach_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })