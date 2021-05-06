from django.shortcuts import render

posts = [
    {'author': 'Corey',
     'title': 'Title1',
     'date': '20.05',
     },
    {'author': 'Schafer',
     'title': 'Title2',
     'date': '21.06',
     },
]


def home(request):
    context = {'post': posts}
    return render(request, 'posts/home.html', context)


def about(request):
    return render(request, 'posts/about.html')
