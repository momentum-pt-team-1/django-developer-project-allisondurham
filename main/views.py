

from django.shortcuts import render
from .models import Todo
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import TodoForm
from django.shortcuts import redirect



def home(request):
    return render(request, 'main/home.html')

def todo_list(request):
    todos = Todo.objects.all().order_by('task')
    return render(request, 'main/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    form = TodoForm()
    return render(request, 'main/todo_detail.html', {'todo': todo, 'form': form})

def todo_new(request):
    form = TodoForm()
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            # todo.user = request.user
            # todo.due_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm()
    return render(request, 'main/todo_edit.html', {'form': form})

def todo_edit(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method =="POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            # todo.user = request.user
            # todo.due_date = timezone.now()
            todo.save()
            return redirect('todo_detail', pk=todo.pk)
    else:
        form = TodoForm(instance=todo)
    return render(request, 'main/todo_edit.html', {'form': form})



# def check_box(request):
#     context = {}
#     context['form'] = Done()
#     return render( request, "todo_detail.html", context)

def todo_done(request):
    todos = Todo.objects.all().order_by('done')
    return render(request, 'main/todo_list.html', {'todos': todos})

def todo_user(request):
    todos = Todo.objects.filter(user__id=request.user.id).order_by('done')
    return render(request, 'main/todo_list.html', {'todos': todos})

def todo_date(request):
    todos = Todo.objects.all().order_by('due_date')
    return render(request, 'main/todo_list.html', {'todos': todos})

def todo_users(request):
    todos = Todo.objects.all().order_by('user__username')
    return render(request, 'main/todo_list.html', {'todos': todos})