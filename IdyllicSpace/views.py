from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User


def logIn(request) :    
    if request.method == 'POST':
        usernameNEW = request.POST['username']
        passwordNEW = request.POST['password']
        user = authenticate(request, username=usernameNEW, password=passwordNEW)
        if user is not None :
            login(request, user)
        else :
            messages.info(request, 'Please try again.')

    else :
        return render(request, 'logIn.html')

def createAcc(request) :
    if request.method == 'POST':

        emailNEW = request.POST['email']
        usernameNEW = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        form = SignUpForm(request.POST)
        if form.is_valid():
            return render(request, 'signUpSuccess.html')
        else:
            if User.objects.filter(email=emailNEW).exists():
                messages.info(request, 'This e-mail is ready taken. Please Log In.')

            if User.objects.filter(username=usernameNEW).exists():
                messages.info(request, 'This username is already taken. Please try again with another username.')

            if (pass1 != pass2):
                messages.info(request, "Your password confirmation doesn't match your password.")

            else:
                messages.info(request, "Please try again.")

    else:
        form = SignUpForm()
    
    return render(request, 'createAcc.html')


def signUpSuccess(request) :
    return render(request, 'signUpSuccess.html')

def forgotPassEmail(request) :
    return render(request, 'forgotPass_Email.html')

def forgotPassPassword(request) :
    return render(request, 'forgotPass_Password.html')

def resetPassSuccess(request) :
    return render(request, 'resetPassSuccess.html')

def checkEmailPage(request) :
    return render(request, 'checkEmailPage.html')

@login_required
def enterCode(request) :
    return render(request, 'enterCode.html')

@login_required
def enterSpace(request) :
    return render(request, 'enterSpace.html')

def mapCreate(request) :
    return render(request, 'mapCreate.html')

def mapJoin(request) :
    return render(request, 'mapJoin.html')

def statusLogIn(request) :
    return render(request, 'statusLogIn.html')