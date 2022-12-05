from django.shortcuts import render, get_object_or_404
from .models import Blogs



def all_blogs(request):
    blogs = Blogs.objects.order_by('-date')
    return render(request, 'all_blogs.html',{'blogs':blogs})

def blog_view(request,id):
    blog = get_object_or_404(Blogs, id=id)
    return render(request, 'blog_view.html', {'blog':blog})
