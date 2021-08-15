from django.shortcuts import render, redirect
from .models import NotionModel
from .forms import NotionForm


def Home(request):
    
    notions = NotionModel.objects.all()
    forms = NotionForm
    context = {
        'form' : forms,
        'notion': notions,

    }
    if request.method == 'POST':
        forms = NotionForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('Home')

    return render(request, 'home.html', context)

def Update(request, task_id):
    task = NotionModel.objects.get(id=task_id)
    forms = NotionForm(instance=task)                                                                                                                                                                                                              
    context = {
        'form' : forms,
        'notion': task,
        'task_id': task_id
    }
    if request.method == 'POST':
        forms = NotionForm(request.POST, instance=task)
        if forms.is_valid():
            forms.save()
            return redirect('Home')

    return render(request, 'update.html', context)
                                                                                                                                                                                                                                                                     
def Delete(request, task_id):
    tasks = NotionModel.objects.get(id=task_id)
    context={
        'task': tasks,
        'task_id':task_id,
    }
    if request.method == 'POST':
        tasks.delete()
        return redirect('Home')

    return render(request, 'delete.html', context)
 



    