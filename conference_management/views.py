# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserProfileForm


# Create your views here.
def index(request):
    return HttpResponse("Please implement your index page.")


def user_profile(request):
    form = UserProfileForm()

    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save(commit=False)
            user = request.user
            user.first_name = request.POST['first_name']
            user.last_name = request.POST['last_name']
            print(user.first_name)
            print(user)
            user_profile.save()
            user.save()

            return redirect('/')
    else:
        print(form.errors)

    context_dict = {'form': form}

    return render(request, 'conference_management/profile_registration.html', context_dict)

