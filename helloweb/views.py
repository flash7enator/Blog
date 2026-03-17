from django.shortcuts import render
from django.http import HttpResponse
import datetime

from django.views import View


def get_menu():
    return """
     <a href='/'> home </a>
     <a href='/datetime'> time </a>
"""


def index(request):
    context = {}
    return render(request, 'helloweb/index.html', context=context)


def page(request):
    context = {}
    return render(request, 'helloweb/page.html', context=context)


def archive(request):
    context = {}
    return render(request, 'helloweb/archives.html', context=context)


def blog(request):
    context = {}
    return render(request, 'helloweb/blog.html', context=context)


data = [1, 2, 3]


def current_datetime(request):
    now = datetime.datetime.now()
    return HttpResponse(get_menu() + f"""
           <h1>Current datetime : {now}</h1>
           <p>Data {data} </p>
    """)


class CurrentDateTime(View):

    def get(self, request):
        now = datetime.datetime.now()
        return HttpResponse(f"""
                   <h1>Current datetime : {now}</h1>
                   <p>Data {data} </p>
            """)
