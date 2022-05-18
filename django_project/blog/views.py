from multiprocessing import context
from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# posts=[
#     {
#         'author' : 'CoreyMS',
#         'title' : 'Blog Post 1',
#         'content' : 'First post content',
#         'date_posted' : 'May 10, 2022',
#     },
#     {
#         'author' : 'Jane Doe',
#         'title' : 'Blog Post 2',
#         'content' : 'Second post content',
#         'date_posted' : 'May 11, 2022',
#     }
# ]

def home(request):
    context={
        'posts' : Post.objects.all()
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request, 'blog/home.html',context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request, 'blog/about.html',{'title': 'About'})
