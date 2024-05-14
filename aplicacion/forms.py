from django.forms import ModelForm
from .models import Cursos

class FormularioCursos(ModelForm):
    class Meta:
        model = Cursos
        fields = ['nombre', 'descripcion', 'duracion', 'link', 'creador']