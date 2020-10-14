from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic.base import View

from task.forms import TaskForm
from task.models import Task


class TaskList(View):
    def get(self, request):
        form = TaskForm()
        tasks = Task.objects.all()
        return render(request, 'task/task_list.html', {
            'form': form,
            'tasks': tasks
        })

    def post(self, request):
        form = TaskForm(request.POST)

        if form.is_valid():
            new_task = form.save()
            return JsonResponse({'task': model_to_dict(new_task)}, status=200)
            # model_to_dict is used to serialize python objects to json
        else:
            return redirect('task_list_url')

class TaskComplete(View):
    def post(self, request, id):
        task = Task.objects.get(id=id)
        task.completed = True
        task.save()
        return JsonResponse({'task': model_to_dict(task)}, status=200)

class TaskDelete(View):
    def post(self, request, id):
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse({'result': 'ok'}, status=200)