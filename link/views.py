from django.shortcuts import render
from .models import Link
from .forms import LinkForm
from django.contrib.auth.models import User
from django.contrib import messages


def HomePage(request):
    return render(request, 'link/home.html', {'title': 'Главная страница'})


def LinkPage(request):
    Links = Link.objects.filter(user=request.user)
    if request.method == 'POST':
        linkP = request.POST.copy()
        linkP['user'] = request.user
        request.POST = linkP
        form = LinkForm(request.POST)

        if form.is_valid():
            SLink = form.cleaned_data.get('short_link')
            flag = 0
            for short_link in Links:
                if SLink == str(short_link):
                    flag = 1
                    break
            if flag == 1:
                messages.error(request, 'Такая ссылка уже существует!')
            else:
                form.save()
                messages.success(request, 'Ссылка успешно сокращена!')
                NewL = Link.objects.filter(user=request.user)
                form = LinkForm()
                return render(request, 'link/short.html', { 'form': form, 'Links': NewL})
        form = LinkForm()
    else:
        form = LinkForm()
    return render(request, 'link/short.html', { 'form': form, 'Links': Links})

