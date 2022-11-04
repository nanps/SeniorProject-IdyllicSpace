from django.shortcuts import render, redirect

def logIn(request) :
    return render(request, 'logIn.html')

def createAcc(request) :
    return render(request, 'createAcc.html')
