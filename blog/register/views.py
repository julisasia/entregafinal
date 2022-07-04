from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def login_request(request):

    if request.method == "POST":

        mi_formulario = AuthenticationForm( request,data = request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            user=authenticate(username=datos.get("username"),password=datos.get ("password") )
            if not user:
                return render( request, "login.html", {"form":mi_formulario,"error":True})
            login(request, user)
            return redirect("/pages")
    mi_formulario = AuthenticationForm()

    return render( request, "login.html", {"form":mi_formulario})

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            form.save()
            login(request, form.instance)
            return redirect("/")

    else:
        form=UserCreationForm()

    return render(request,"registro.html", {"form":form})

def logout_request(request):
    logout(request)
    return redirect("/")
