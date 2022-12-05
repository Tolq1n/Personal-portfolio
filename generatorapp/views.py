from django.shortcuts import render
import random

# Create your views here.


def home2(request):
    return render(request, "home2.html")

def password(request):
    characters = list('abcdefghijklmnopqrstuvxyz')

    if request.GET.get('big'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVXYZ'))
    if request.GET.get('number'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('!@#$%^&*()'))

    uzunliki = int(request.GET.get('uzunlik'))

    thepassword = ''

    for x in range(int(uzunliki)):
        thepassword += random.choice(characters)

    return render(request, "password.html", {'password':thepassword} )
