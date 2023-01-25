from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserManage
from django.contrib.auth.models import User
from .forms import DisplayNameForm, AvatarForm


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
