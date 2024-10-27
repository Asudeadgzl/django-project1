from django.shortcuts import render

posts= [
    
    {
        'author': 'CoreyMS',
        'title': 'BlogPost 1', 
        'content': 'First Post Content',
        'date_posted': 'August 27, 2023'
    },
       {
        'author': 'Jane Doe',
        'title': 'BlogPost 2', 
        'content': 'Second Post Content',
        'date_posted': 'August 28, 2023'
    }
]


def home(request):
    context= {
        'posts': posts
    }
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


