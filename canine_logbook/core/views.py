from django.shortcuts import render


def dashboard(request):

    return render(request, 'core/dashboard.html',{
    })


def auth(request):

    return render(request, 'core/auth.html', {
    })


def add_dog(request):

    return render(request, 'core/add_dog.html')
