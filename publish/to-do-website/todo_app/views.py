from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def TodoView(request):
    c1 = Todo.objects.all()
    return render(request, 'todo_app/todo_page.html', {"todolist": c1})


def TodoAdd(request):
    c1 = Todo(content = request.POST["content"])
    c1.save()
    return redirect("todoview")

def TodoDelete(request, id):
    c1 = Todo.objects.get(id = id)
    c1.delete()
    return redirect("todoview")
