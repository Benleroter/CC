from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, ProfileUpdateForm2




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'clients/register.html', {'form': form})

@login_required
def clientprofile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.clientprofile)
        #d_form = ProfileUpdateForm2(frequest.POST, request.FILES, instance=request.user.clientprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated')
            return redirect('clientprofile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.clientprofile)
    #    d_form = ProfileUpdateForm2(instance=request.user.clientprofile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    #    'd_form': d_form
    }
    return render(request, 'clients/clientprofile.html', context)

def clientprofileview(request):
    return render(request, 'clients/clientprofileview.html', {'title': 'ProfileView'})