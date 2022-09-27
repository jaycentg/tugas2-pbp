from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from todolist.models import Task
from django.contrib.auth.decorators import login_required

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_data = Task.objects.filter(user = request.user)
    context = {
        'task_list': task_data,
        'username': request.user,
    }
    return render(request, "todolist.html", context)

# Create your views here.
def register(request):
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    return redirect('todolist:login')

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        # request.user refers to current logged-in user
        user = request.user
        # request.POST.get akan mengembalikan None jika 'taskname' tidak ada pada request.POST
        title = request.POST.get('taskname')
        description = request.POST.get('taskdesc')
        task = Task.objects.create(user=user, title=title, description=description)
        messages.success(request, "Successfully add new task")
        return redirect('todolist:show_todolist')
    context = {}
    return render(request, 'new_task.html', context)

def delete_task(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('todolist:show_todolist')

def change_status(request, id):
    task = Task.objects.get(id=id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')