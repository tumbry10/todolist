from django.shortcuts import render, redirect
from .forms import TaskCartegoryCreationForm, TaskCreationForm
from . models import TaskCartegory, Task

# Create your views here.
def taskList(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'main/task_list.html', context)

def cartegoryCreate(request):
    if request.method == 'POST':
        form = TaskCartegoryCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cartegoryList')
        else:
            return render(request, 'main/cartegory_create.html', {'form': form})
    else:
        form = TaskCartegoryCreationForm()
        return render(request, 'main/cartegory_create.html', {'form': form})

def cartegoryList(request):
    cartegories = TaskCartegory.objects.all()
    context = {'cartegories': cartegories}
    return render(request, 'main/cartegory_list.html', context)

def taskCreate(request):
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('taskList')
        else:
            return render(request, 'main/task_create.html', {'form': form})
    else:
        form = TaskCreationForm()
        return render (request, 'main/task_create.html', {'form': form})

