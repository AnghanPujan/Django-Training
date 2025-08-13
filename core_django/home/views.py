from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    people=[
        {'name': 'John', 'age': 30},
        {'name': 'Jane', 'age': 25},
        {'name': 'Doe', 'age': 22},
        {'name': 'John', 'age': 13},
        {'name': 'Jane', 'age': 15},
        {'name': 'Doe', 'age': 22}
    ]

    context = {'people': people, 
               'text': 'home_page is returned by Django',
               'page': 'Django _Tutorial'
               }
    return render(request, "home/index.html", context)

def success_page(request):
    context = {
        'text': 'sucess_page is returned by Django',
        'page' : 'sucess_page'
        }
    return render(request, "home/index.html", context)

def about(request):
    context = {
        'text': 'about_page is returned by Django',
        'page' : 'about_page'
    }
    return render(request, "home/about.html", context)

def contact(request):
    context = {
        'text': 'contact_page is returned by Django',
        'page' : 'contact_page'
        }
    return render(request, "home/contact.html", context)