from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import Userss

# Create your views here.

def index(request):
    return render(request, 'index.html', )

def addusers(request):
   
    if request.method == 'POST':
        form = Userss(request.POST)
        if form.is_valid():
            user=form.save()
        # return HttpResponseRedirect('/thanks/')
        return redirect(user)

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = Userss(request.POST)
#         # check whether it's valid:
#         # if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#         return HttpResponseRedirect('/thanks/')

#     # # if a GET (or any other method) we'll create a blank form
#     # else:
    #     form = Userss()

    # return render(request, 'name.html', {'form': form})