from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from pages.models import Blog
from pages.forms import Blogs_formulario, BlogForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def inicio(request):
    plantilla = loader.get_template("inicio.html")
    dicc = {"user":request.user}
    documento = plantilla.render(dicc)
    return HttpResponse( documento )


def about(request):
    plantilla = loader.get_template("about.html")
    dicc = {"user":request.user}
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

def listar_pages(request):
    return HttpResponse("HOLA")

def listar_pages(request):
    blogs = Blog.objects.all()
    dicc = {"blogs" : blogs, "user":request.user}
    plantilla = loader.get_template("blogs.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

def ver_page(request, id):
    blog = Blog.objects.get(id=id)
    dicc = {"blog" : blog, "user":request.user}
    plantilla = loader.get_template("blog_detalle.html")
    documento = plantilla.render(dicc)
    return HttpResponse( documento )

@login_required (login_url='login_name')
def crear_page(request,id=None):
    blog = None
    if request.method=="POST":
        form=BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.instance.fecha_creacion = datetime.now()
            form.save()
            return redirect("/pages")

    else:
        form=BlogForm(instance=blog)

    return render(request,"edit_page.html", {"form":form,"user":request.user})

@login_required (login_url='login_name')
def editar_page(request, id):
    blog = Blog.objects.get(id=id)
    if request.method=="POST":
        form=BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.instance.fecha_creacion = datetime.now()
            form.save()
            return redirect("/pages")

    else:
        form=BlogForm(instance=blog)

    return render(request,"edit_page.html", {"form":form,"user":request.user, "boton":"Guardar"})

@login_required (login_url='login_name')
def eliminar_page(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("/pages")

