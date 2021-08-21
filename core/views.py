from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Show
from time import strftime, strptime
from datetime import date, datetime

def index(request):
    return redirect("/shows")

def shows(request):
    context = {
        "all_shows": Show.objects.all(),
    }
    print(context)
    return render(request, "shows.html", context)

def add(request):
    return render(request, "add.html")

def create(request):
    #Chequeamos los errores primero
    errors = Show.objects.basic_validator(request.POST)
    #si el largo de los errores es mayor a cero manda un mensaje
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/shows/new")

    else:
        new_show = Show.objects.create(title= request.POST['title'], network= request.POST['network'], release_date= request.POST['releasedate'], desc= request.POST['desc'])
        print(new_show.id)
        return redirect(f"/shows/{new_show.id}")

def show(request, show_id):
    show = Show.objects.get(id=show_id)
    #format time for field to display as M/DD/YYYY
    release_format = show.release_date.strftime('%B %d, %Y')
    context = {
        "release_date_format": release_format,
        "this_show": show,
    }
    return render(request, "show.html", context)

def edit(request, show_id):
    show = Show.objects.get(id=show_id)
    release_format = show.release_date.strftime('%m/%d/%Y')
    context = {
        "this_show": show, 
        "release_date_format": release_format
    }
    return render(request, "edit.html",context)

def update(request, show_id):

    errors = Show.objects.basic_validator(request.POST)
    if len(errors)> 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f"/{show_id}/edit")
    else:
        input_date= request.POST['releasedate']
        current_date= datetime.strptime(input_date, '%m/%d/%Y')
        format_date= current_date.strftime('%Y-%m-%d')
        update = Show.objects.get(id= show_id)
        update.title = request.POST['title']
        update.network = request.POST['network']
        update.release_date = format_date
        update.desc = request.POST['desc']
        update.save()
        return redirect(f"/shows/{show_id}")

def delete(request, show_id):
    show_to_delete = Show.objects.get(id= show_id)
    show_to_delete.delete()
    return redirect("/shows")