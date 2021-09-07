# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from authors.models import Authors


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            user = form.save(commit=False)
            messages.success(request, 'Account created for {0}!'.format(username))
            user_group = Group.objects.get(name=form.cleaned_data.get('groups'))
            user.groups.add(user_group)
            if user_group.name == 'Authors':
                auth = Authors()
                auth.first_name = request.POST.get("first_name")
                auth.last_name = request.POST.get("last_name")
                auth.biography = "..."
                auth.save()
            return redirect('about')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'user/profile.html', context)
