from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def home_page(request):
    template_vars = {'version': settings.VERSION}
    return render(request, 'home_page.html', template_vars)
