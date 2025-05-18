from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskCartegoryCreationForm, TaskCreationForm, TaskEditForm, TaskCartegoryEditForm
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
    
def editTask(request, id):
    task = Task.objects.get(id=id)
    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('taskList')
    else:
        form = TaskEditForm(instance=task)
    context = {
        'form': form,
        'task': task,
    }
    return render(request, 'main/edit_task.html', context)

def editCategory(request, id):
    cartegory = TaskCartegory.objects.get(id=id)
    if request.method == 'POST':
        form = TaskCartegoryEditForm(request.POST, instance=cartegory)
        if form.is_valid():
            form.save()
            return redirect('cartegoryList')
    else:
        form = TaskCartegoryEditForm(instance=cartegory)
        context = {
            'form': form,
            'cartegory': cartegory,
        }
        return render(request, 'main/edit_cartegory.html', context)


def deleteTask(request, id):
    task = Task.objects.get(id=id)
    task.delete()
    return redirect('taskList')

def deleteCategory(request, id):
    cartegory = TaskCartegory.objects.get(id=id)
    cartegory.delete()
    return redirect('cartegoryList')
