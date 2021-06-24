from django.shortcuts import render, redirect

# Create your views here.
from typing import Any

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


from django.contrib.auth import authenticate as auth

from rentalsite.models import Category


def login(request):
    if request.user.is_authenticated():
        return redirect('base.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('base.html')
        else:
            print('Invalid login credentials')
    return render(request, 'login.html')


# class based views

class ListModules(ListView):  # generic view
    template_name = 'rentalmanagement/list_modules_class_view.html'
    model = Category
    context_object_name = 'modules'

