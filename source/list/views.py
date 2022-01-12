from django.shortcuts import render, redirect, get_object_or_404
from list.models import Task
from list.forms import TaskForm, TaskFormDelete
# Create your views here.
def home_page(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks' : tasks})

def task_view(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'view.html', {'task' : task})

def create(request):
    if request.method == 'GET':
        form = TaskForm()
        return render(request, 'create.html', {'form' : form})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            description = form.cleaned_data.get('description')
            status = form.cleaned_data.get('status')
            date = form.cleaned_data.get('date')
            detail = form.cleaned_data.get('detail')
            Task.objects.create(description=description,
                               status=status,
                               date=date,
                                detail=detail)
            return redirect('home_page')
        return render(request, 'create.html', {'form' : form})

def delete(request, pk):
    confirm = 'ДА'
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskFormDelete()
        return render(request, 'delete.html', {'task' : task, 'form' : form})
    else:
        form = TaskFormDelete(data=request.POST)
        if form.is_valid():
            if form.cleaned_data.get('confirm') != confirm:
                form.errors['confirm'] = ['Вы ввели другое слово']
                return render(request, 'delete.html', {'form': form, 'task' : task})
            task.delete()
            return redirect('home_page')
        return render(request, 'delete.html', {'form' : form, 'task' : task})

def update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'GET':
        form = TaskForm(initial={
            'description' : task.description,
            'status': task.status,
            'date': task.date,
            'detail': task.detail,
        })
        return render(request, 'update.html', {'form' : form, 'task' : task})
    else:
        form = TaskForm(data=request.POST)
        if form.is_valid():
            task.description = form.cleaned_data.get('description')
            task.status = form.cleaned_data.get('status')
            task.date = form.cleaned_data.get('date')
            task.detail = form.cleaned_data.get('detail')
            task.save()
            return redirect('view', pk=task.pk)
        return render(request, 'update.html', {'task' : task, 'form' : form})