from django.shortcuts import render, redirect
from .forms import UserRegForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = UserRegForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Пользователь {username} был успешно создан!')
            return redirect('user')
        else:
            messages.error(request, 'Вы ввели некорректные данные!')


    else:
        form = UserRegForm()


    return render(request, 'users/registration.html',
    {
        'title': 'Страница регистрации',
        'form': form
    })


@login_required
def profile(request):
    if request.method == "POST":
        updateUserForm = UserUpdateForm(request.POST, instance=request.user)

        if updateUserForm.is_valid():
            updateUserForm.save()
            messages.success(request, f'Ваш аккаунт был успешно обновлён!')
            return redirect('profile')
    else:
        updateUserForm = UserUpdateForm(instance=request.user)
    data = {
        'updateUserForm': updateUserForm
    }

    return render(request, 'users/profile.html', data)