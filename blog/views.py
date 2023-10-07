from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def index(request):
    return render(request, 'blog/index.html', {})


def index2(request):
    return render(request, 'blog/index2.html', {})


def index3(request):
    return render(request, 'blog/index3.html', {})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Данная страница не найдена, проверьте правильность написании индекса!</h1>')


def categ(request, catid):
    print(request.NAME, "<<<<")
    print(request.lastname, "<<<<")
    return HttpResponse(f'<h1>page{catid}</h1>')
# Create your views here.
