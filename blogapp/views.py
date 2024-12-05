from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Blog
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.


def home(request):
    blogs = Blog.objects.all()  # Recuperar todos los blogs
    return render(request, 'blogapp/home.html', {'blogs': blogs})


def blog_detail(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    return render(request, 'blogapp/blog_detail.html', {'blog': blog})


def about(request):
    return render(request, 'blogapp/about.html')


# Vista para crear un blog
@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Blog creado exitosamente!")
            return redirect('home')
    else:
        form = BlogForm()
    return render(request, 'blogapp/blog_form.html', {'form': form, 'action': 'Crear'})


# Vista para editar un blog
@login_required
def blog_update(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Blog actualizado exitosamente!")
            return redirect('blog_detail', blog_id=blog.id)
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blogapp/blog_form.html', {'form': form, 'action': 'Editar'})


# Vista para borrar un blog
@login_required
def blog_delete(request, blog_id):
    blog = get_object_or_404(Blog, id=blog_id)
    if request.method == 'POST':
        blog.delete()
        messages.success(request, "¡Blog eliminado exitosamente!")
        return redirect('home')
    return render(request, 'blogapp/blog_confirm_delete.html', {'blog': blog})
