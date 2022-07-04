from django import forms
from .models import Blog  

class Blogs_formulario(forms.Form):

    titulo = forms.CharField(max_length=40)
    subtitulo = forms.CharField(max_length=40)
    cuerpo = forms.CharField(max_length=400)
    autor = forms.CharField(max_length=20)

class BlogForm(forms.ModelForm):
    class Meta:
         model = Blog
         fields = ['titulo', 'subtitulo', 'autor', 'cuerpo', 'imagen']

