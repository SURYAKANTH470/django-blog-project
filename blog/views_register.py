from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('blog_list')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})