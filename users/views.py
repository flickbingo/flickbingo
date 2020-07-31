from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hey {username}!, your account has been created. Please login with your credentials...')
            return redirect('users-login')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been UPDATED.')
            return redirect('users-profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    content = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html',content)

def search(request):
    if request.method == 'GET':
        search = request.GET['search']
        if search:
            match = User.objects.filter(username__icontains = search)
            if match:
                return render(request,'users/search.html',{'match':match})
            else:
                messages.error(request, f'No results FOUND!')
        else:
            return redirect('flick-home')
    return redirect('flick-home')