from django.shortcuts import render, get_object_or_404
from . models import blog

def all_blogs(request):
    blogs= blog.objects.order_by('-date')
    return render (request, 'blogs/all_blogs.html',{'blogs':blogs} )

def detail(request, blog_id):
    blogs = get_object_or_404(blog, pk=blog_id)
    return render (request, 'blogs/detail.html',{'blogs':blogs})