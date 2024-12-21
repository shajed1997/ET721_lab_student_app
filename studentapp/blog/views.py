from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogForm

def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, "blog/blog_list.html", {"blogs": blogs})

def blog_detail(request, pk):
    blog = BlogPost.objects.get(pk=pk)
    return render(request, "blog/blog_detail.html", {"blog": blog})

def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("blog_list")
    else:
        form = BlogForm()
    return render(request, "blog/add_blog.html", {"form": form})
