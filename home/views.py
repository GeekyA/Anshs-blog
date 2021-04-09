from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post

# Create your views here.


def posts(request):
    all_posts = Post.objects.order_by('-date_pub')
    context = {'all_posts':all_posts}
    return render(request,'home/index.html',context)


def content(request,post_id):
    post = get_object_or_404(Post,pk=post_id)
    context = {"post":post}
    #print(post.content)
    return render(request,'home/content.html',context)

def search_results(request):
    import re
    if request.method=='GET':
        query = request.GET.get("tag")
    all_posts = Post.objects.all()
    filtered = []
    for post in all_posts:
        if str(query) in str(post.title) or str(query) in str(post.content):
            filtered.append(post)
    return render(request,'home/results.html',{'filtered':filtered})
    


