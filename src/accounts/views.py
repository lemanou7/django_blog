from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import UserRegisterForm, UserLoginForm

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST or None)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has been created, You can now log in!')
            return redirect('accounts:login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


