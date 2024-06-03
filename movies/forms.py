from django.forms import ModelForm
from .models import Movie,Info, Comment

class commentForm(ModelForm):
    class Meta:
        model = Comment
        fields =['comment','rate']


class movieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title','year','description','rating','pictures']

class InfoForm(ModelForm):
    class Meta:
        model= Info
        fields = ["kind","age"]
