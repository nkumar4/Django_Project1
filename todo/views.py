from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect


def todo(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('Item added to the list!!'))
            return render(request, 'todo.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'todo.html', {'all_items': all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item deleted from the list!!'))
    return redirect('todo')


def crossed(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('todo')


def uncrossed(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('todo')


def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, ('Item edited!!'))
            return redirect('todo')
    else:
        edit_item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'edit_item': edit_item})
