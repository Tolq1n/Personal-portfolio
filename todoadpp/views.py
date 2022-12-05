from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import ToDoForm
from .models import ToDo
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home1(request):
    return render(request, 'todos/home1.html')

@login_required
def currenttodos(request):
    todos = ToDo.objects.filter(user=request.user, datecompleted__isnull=True)
    return render(request, 'todos/currenttodos.html', {'todos':todos})

@login_required
def viewtodos(request,id):
    todo = get_object_or_404(ToDo, id=id, user=request.user)
    if request.method == "GET":
        form = ToDoForm(instance=todo)
        return render(request, 'todos/viewtodos.html', {'todo':todo, 'form':form})
    else:
        try:
            form = ToDoForm(request.POST, instance=todo)
            form.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todos/viewtodos.html', {'todo':todo, 'form':form, 'error':'Bad info'})

@login_required
def complatetodos(request, id):
    todo = get_object_or_404(ToDo, id=id, user=request.user)
    if request.method == 'POST':
        todo.datecompleted = timezone.now()
        todo.save()
        return redirect('currenttodos')

@login_required
def comptodos(request):
    todos = ToDo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, 'todos/comptodos.html', {'todos':todos})

@login_required
def deletetodos(request, id):
    todo = get_object_or_404(ToDo, id=id, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('currenttodos')

@login_required
def createtodos(request):
    if request.method == 'GET':
        return render(request, 'todos/createtodos.html', {'form':ToDoForm()})
    else:
        try:
            form = ToDoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect('currenttodos')
        except ValueError:
            return render(request, 'todos/createtodos.html', {'form':ToDoForm(), 'error':'Bad date is passed.Please try again.'})

def signupuser(request):
        try:
            if request.method == 'GET':
                return render(request, 'registration/signup.html', {'form':UserCreationForm()})
            else:
                if (request.POST['password1'] != None and request.POST['password1'] == request.POST['password2']):
                    try:
                        user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                        user.save()
                        login(request,user)
                        return redirect('currenttodos')
                    except IntegrityError:
                        return render(request, 'registration/signup.html', {'form':UserCreationForm(), 'error':'It is not uniqe username.'})
                else:
                    return render(request, 'registration/signup.html', {'form':UserCreationForm(), 'error':'Password didn\'t match'})
                    # Password didn't match
        except ValueError:
            return render(request, 'registration/signup.html', {'form':UserCreationForm(), 'error':'The given username must be set'})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home1')

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'registration/loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'registration/loginuser.html', {'form':AuthenticationForm(), 'error':'Username or password did not match.'})
        else:
            login(request,user)
            return redirect('currenttodos')
