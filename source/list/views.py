from django.shortcuts import render, redirect, get_object_or_404
from list.models import Task
from list.forms import TaskForm
# Create your views here.
def home_page(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks' : tasks})

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
            Task.objects.create(description=description,
                               status=status,
                               date=date)
            return redirect('home_page')
        return render(request, 'create.html', {'form' : form})

def delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('home_page')