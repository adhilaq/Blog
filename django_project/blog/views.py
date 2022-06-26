from django.http import HttpResponse
from django.shortcuts import render

posts = [
    {
        'title': 'Blog Post 1',
        'author':'Adhil',
        'date_posted': '26 June 2022',
        'content': 'First post content'
    },
    {
        'title': 'Blog Post 2',
        'author':'Pavan',
        'date_posted': '27 June 2022',
        'content': 'Second post content'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

