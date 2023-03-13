from django.http import HttpResponse
from  django.shortcuts import render, redirect
from .models import OrderCharger
from .forms import OrderChargerFrom




def index(request):
    chagers = OrderCharger.objects.all()

    return render(request, 'hello/index.html', {'title':'Главная страница сайта', 'chagers': chagers})


def about(request):
    return render(request, 'hello/about.html')




def map(request):
    return render(request, 'hello/map.html')




def create(request):
    error = ''
    if request.method == 'GET':
        form = OrderChargerFrom(request.GET)
        if form.is_valid():
            form.save()
            #return redirect('home')
        else:
            error = "Форма не верна!"
    form = OrderChargerFrom()
    context = {
        'form': form
    }
    return render(request, 'hello/create.html', context)