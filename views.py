from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'tasks': tasks})


@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        if title:
            Task.objects.create(
                user=request.user,
                title=title,
                description=description
            )

    return redirect('tasks:dashboard')   # ✅ FIXED


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('tasks:dashboard')


@login_required
def update_status(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == "POST":
        status = request.POST.get('status')
        if status in ['Pending', 'In-Progress', 'Done']:
            task.status = status
            task.save()

    return redirect('tasks:dashboard')

@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == "POST":
        task.title = request.POST.get('title')
        task.description = request.POST.get('description')
        task.save()
        return redirect('tasks:dashboard')

    return render(request, 'edit_task.html', {'task': task})
