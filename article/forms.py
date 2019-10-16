from django import forms
from .models import Article
class ArticleForm(forms.ModelForm):
    
    class Meta: #bu sayede birde custom form yaratmiriq modeli olanlarinki cox qisa kodla yaranmis olur
        model=Article
        fields=["title","content","article_image"]