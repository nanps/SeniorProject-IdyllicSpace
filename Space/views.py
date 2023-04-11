from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SpaceRoom, UserManage, ChatMessage, RoomMember
from django.contrib.auth.models import User
from .forms import SpaceRoomForm, DisplayNameForm, AvatarForm, BioForm, CurrentSpaceRoomForm, MessageForm, MoodForm, LeaveRoomForm
from django.contrib import messages

from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
import json
from django.views.decorators.csrf import csrf_exempt

def getToken(request):
    appId = "d176f6cd28f04644afa6d6093551c6d4"
    appCertificate = "fd2591d725e44459a51d6a4b3bded8e0"
    channelName = request.GET.get('channel')
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName, uid, role, privilegeExpiredTs)

    return JsonResponse({'token': token, 'uid': uid}, safe=False)

@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )

    return JsonResponse({'name':data['name']}, safe=False)

def getMember(request):
    uid = request.GET.get('UID')
    room_name = request.GET.get('room_name')

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({'name':member.name}, safe=False)

@csrf_exempt
def deleteMember(request):
    data = json.loads(request.body)
    member = RoomMember.objects.get(
        name=data['name'],
        uid=data['UID'],
        room_name=data['room_name']
    )
    member.delete()
    return JsonResponse('Member deleted', safe=False)


# Create your views here.
@login_required
def home(request) :   

    usernameInput = request.user 

    if request.method == 'POST':

        if (UserManage.objects.filter(username=usernameInput).exists()) :
            return redirect('enterSpace')
        else :
            return redirect('maleAvatar')

    return render(request, 'home.html')

@login_required
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

@login_required
def userProfilePage(request) :
    usernameInput = request.user

    userData = UserManage.objects.get(username=usernameInput)

    if request.method == 'POST':

        moodForm = MoodForm(request.POST)
        if moodForm.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instanceMood = moodForm.save(commit=False)
                instanceMood.username = request.user
                instanceMood.save(update_fields=['mood'])

                return render(request, 'userProfilePage.html', {'userData':userData})
                
        DNform = DisplayNameForm(request.POST)
        if DNform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = DNform.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['displayName'])

                return render(request, 'userProfilePage.html', {'userData':userData})

        BIOform = BioForm(request.POST)
        if BIOform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instanceBio = BIOform.save(commit=False)
                instanceBio.username = request.user
                instanceBio.save(update_fields=['bio'])

                return render(request, 'userProfilePage.html', {'userData':userData})

    return render(request, 'userProfilePage.html', {'userData':userData})

@login_required
def settingPage(request) :
    return render(request, 'settingPage.html')

@login_required
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

@login_required
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

@login_required
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
@login_required
def maleAvatarEdit(request) :
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

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

    return render(request, 'maleAvatar_edit.html', {'userData':userData})

@login_required
def femaleAvatarEdit(request) :
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

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

    return render(request, 'femaleAvatar_edit.html', {'userData':userData})

@login_required
def mysteryAvatarEdit(request) :
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

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

    return render(request, 'mysteryAvatar_edit.html', {'userData':userData})

@login_required
def editAvatarSuccess(request) :
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    return render(request, 'editAvatarSuccess.html', {'userData':userData})

#Edit Avatar Profile
@login_required
def maleAvatar_profile(request) :
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    if request.method == 'POST':
        form = AvatarForm(request.POST)
        if form.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = form.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['avatar'])

                return redirect('userProfilePage')
        else :
            messages.info(request, "You must choose one Avatar.")
    else:
        form = AvatarForm()

    return render(request, 'maleAvatar_profile.html', {'userData':userData})

@login_required
def femaleAvatar_profile(request) :
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    if request.method == 'POST':
        form = AvatarForm(request.POST)
        if form.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = form.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['avatar'])

                return redirect('userProfilePage')
        else :
            messages.info(request, "You must choose one Avatar.")
    else:
        form = AvatarForm()

    return render(request, 'femaleAvatar_profile.html', {'userData':userData})

@login_required
def mysteryAvatar_profile(request) :
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    if request.method == 'POST':
        form = AvatarForm(request.POST)
        if form.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():

                instance = form.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['avatar'])

                return redirect('userProfilePage')
        else :
            messages.info(request, "You must choose one Avatar.")
    else:
        form = AvatarForm()

    return render(request, 'mysteryAvatar_profile.html', {'userData':userData})

# map
@login_required
def mapCreate(request) :
    return render(request, 'mapCreate.html')





# --------------- CLASSROOM (CREATE) ---------------
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
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
@login_required
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

@login_required
def Classroom_Confirm(request):
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    rooms = SpaceRoom.objects.all()
    for room in rooms :
        if room.slug in userData.currentSpaceRoom :
            room.inRoom += 1
            room.save()

    return render(request, 'classroom_rooms_confirm.html', {'rooms':rooms, 'userData':userData, })

@login_required
def Room(request, roomName):
    room = SpaceRoom.objects.get(roomName=roomName)

    return render(request, 'room.html', {'room':room})

# --------------- FOREST (JOIN) ---------------
@login_required
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

@login_required
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
@login_required
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

@login_required
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
@login_required
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

@login_required
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
@login_required
def Beach_Rooms(request):
    rooms = SpaceRoom.objects.all()

    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    usernameInput = request.user
    if request.method == 'POST':
        nameNEW = userData.displayName
        room_nameNEW = request.POST['currentSpaceRoom']
        newRoomMember = RoomMember.objects.create(name=nameNEW, room_name=room_nameNEW)
        newRoomMember.save()


        CSRform = CurrentSpaceRoomForm(request.POST)
        if CSRform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = CSRform.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['currentSpaceRoom'])
            return redirect('beachConfirm')

    return render(request, 'beach_rooms.html', {'rooms':rooms, 'userData':userData, })

@login_required
def Beach_Confirm(request):
    usernameInput = request.user
    userData = UserManage.objects.get(username=usernameInput)

    rooms = SpaceRoom.objects.all()
    for room in rooms :
        if room.slug in userData.currentSpaceRoom :
            slug = room.slug

            room.inRoom += 1
            room.save()

            if (room.inRoom == room.capacity) :
                SpaceRoom.objects.filter(slug=slug).update(roomStatus = "full")

    return render(request, 'beach_rooms_confirm.html', {'rooms':rooms, 'userData':userData, })




# --------------- CLASSROOM (SPACE) ---------------
@login_required
def Classroom_Space(request, slug):
    room = SpaceRoom.objects.get(slug=slug)

    return render(request, 'classroom_space.html', {'room': room})

# --------------- FOREST (SPACE) ---------------
@login_required
def Forest_Space(request, slug):
    room = SpaceRoom.objects.get(slug=slug)
    slugValue = room.slug

    ChatMessages = ChatMessage.objects.filter(slug=slugValue) 

    usernameInput = request.user

    userData = UserManage.objects.get(username=usernameInput)
    user = User.objects.get(username=usernameInput)

    currSpaceValue = "Space/Forest/" + slug
    members = UserManage.objects.filter(currentSpaceRoom=currSpaceValue)

    if request.method == 'POST':

        leaveForm = LeaveRoomForm(request.POST)
        if leaveForm.is_valid() :
            if SpaceRoom.objects.filter(slug=slug).exists():
                UserManage.objects.filter(username=usernameInput).update(currentSpaceRoom="None")
                
                instanceinRoom = leaveForm.save(commit=False)
                instanceinRoom.slug = slug
                instanceinRoom.save(update_fields=['inRoom', 'roomStatus'])

                if request.POST['roomStatus'] == "close" :
                    SpaceRoom.objects.get(slug=slug).delete()
                    ChatMessages.delete()

                return redirect('enterSpace')
            
        chatForm = MessageForm(request.POST)
        if chatForm.is_valid() :
            chatForm.instance.displayName = userData
            chatForm.save()

            return render(request, 'forest_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })
    
        moodForm = MoodForm(request.POST)
        if moodForm.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instanceMood = moodForm.save(commit=False)
                instanceMood.username = request.user
                instanceMood.save(update_fields=['mood'])

                return render(request, 'forest_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })
            
        DNform = DisplayNameForm(request.POST)
        if DNform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = DNform.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['displayName'])

                return render(request, 'forest_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, })
        # else :
        #     messages.info(request, "Display Name cannot be blank.")

        BIOform = BioForm(request.POST)
        if BIOform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instanceBio = BIOform.save(commit=False)
                instanceBio.username = request.user
                instanceBio.save(update_fields=['bio'])

                return render(request, 'forest_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })

    return render(request, 'forest_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })

# --------------- CAFE (SPACE) ---------------
@login_required
def Cafe_Space(request, slug):
    room = SpaceRoom.objects.get(slug=slug)
    slugValue = room.slug

    ChatMessages = ChatMessage.objects.filter(slug=slugValue) 

    usernameInput = request.user

    userData = UserManage.objects.get(username=usernameInput)
    user = User.objects.get(username=usernameInput)

    currSpaceValue = "Space/Cafe/" + slug
    members = UserManage.objects.filter(currentSpaceRoom=currSpaceValue)

    if request.method == 'POST':

        leaveForm = LeaveRoomForm(request.POST)
        if leaveForm.is_valid() :
            if SpaceRoom.objects.filter(slug=slug).exists():
                UserManage.objects.filter(username=usernameInput).update(currentSpaceRoom="None")
                
                instanceinRoom = leaveForm.save(commit=False)
                instanceinRoom.slug = slug
                instanceinRoom.save(update_fields=['inRoom', 'roomStatus'])

                if request.POST['roomStatus'] == "close" :
                    SpaceRoom.objects.get(slug=slug).delete()
                    ChatMessages.delete()

                return redirect('enterSpace')
            
        chatForm = MessageForm(request.POST)
        if chatForm.is_valid() :
            chatForm.instance.displayName = userData
            chatForm.save()

            return render(request, 'cafe_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })
    
        moodForm = MoodForm(request.POST)
        if moodForm.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instanceMood = moodForm.save(commit=False)
                instanceMood.username = request.user
                instanceMood.save(update_fields=['mood'])

                return render(request, 'cafe_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })
            
        DNform = DisplayNameForm(request.POST)
        if DNform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instance = DNform.save(commit=False)
                instance.username = request.user
                instance.save(update_fields=['displayName'])

                return render(request, 'cafe_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, })
        # else :
        #     messages.info(request, "Display Name cannot be blank.")

        BIOform = BioForm(request.POST)
        if BIOform.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instanceBio = BIOform.save(commit=False)
                instanceBio.username = request.user
                instanceBio.save(update_fields=['bio'])

                return render(request, 'cafe_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })

    return render(request, 'cafe_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })

# --------------- LIBRARY (SPACE) ---------------
@login_required
def Library_Space(request, slug):
    room = SpaceRoom.objects.get(slug=slug)

    return render(request, 'library_space.html', {'room': room})

# --------------- BEACH (SPACE) ---------------
@login_required
def Beach_Space(request, slug):
    room = SpaceRoom.objects.get(slug=slug)
    slugValue = room.slug

    ChatMessages = ChatMessage.objects.filter(slug=slugValue) 

    usernameInput = request.user

    userData = UserManage.objects.get(username=usernameInput)
    user = User.objects.get(username=usernameInput)

    currSpaceValue = "Space/Beach/" + slug
    members = UserManage.objects.filter(currentSpaceRoom=currSpaceValue)

    if request.method == 'POST':

        leaveForm = LeaveRoomForm(request.POST)
        if leaveForm.is_valid() :
            if SpaceRoom.objects.filter(slug=slug).exists():
                UserManage.objects.filter(username=usernameInput).update(currentSpaceRoom="None")
                
                instanceinRoom = leaveForm.save(commit=False)
                instanceinRoom.slug = slug
                instanceinRoom.save(update_fields=['inRoom', 'roomStatus'])

                if request.POST['roomStatus'] == "close" :
                    SpaceRoom.objects.get(slug=slug).delete()
                    ChatMessages.delete()

                return redirect('enterSpace')
            
        chatForm = MessageForm(request.POST)
        if chatForm.is_valid() :
            chatForm.instance.displayName = userData
            chatForm.save()

            return render(request, 'beach_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })
    
        moodForm = MoodForm(request.POST)
        if moodForm.is_valid() :
            if UserManage.objects.filter(username=usernameInput).exists():
                instanceMood = moodForm.save(commit=False)
                instanceMood.username = request.user
                instanceMood.save(update_fields=['mood'])

                return render(request, 'beach_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })
            
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

    return render(request, 'beach_space.html', {'room': room, 'userData':userData, 'user':user, 'ChatMessages':ChatMessages, 'members':members, })