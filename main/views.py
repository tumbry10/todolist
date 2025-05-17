from django.shortcuts import render, redirect
from .forms import TaskCreationForm
from . models import Task

# Create your views here.
def taskList(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'main/task_list.html', context)

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