from django.forms import ModelForm
from .models import Article            # Hal-hairki papqanin icindeki models.py faylindan ozumuz yazdigimiz Article metodunu daxil edirik
from django import forms

class ArticleForm(ModelForm):
    class Meta:
        model = Article                # Django documentation seh 252
        fields = ['title', 'content', 'article_image']  # Articldaki 'title', 'content' sahelerinden bir input yarat dedik


class BudceForm(forms.Form):
    budget = forms.CharField(label="Aylıq ailə büdcənizi daxil edin")