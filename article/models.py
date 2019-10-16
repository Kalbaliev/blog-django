from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):

    author=models.ForeignKey("auth.User",on_delete=models.CASCADE,verbose_name="Yazar")
    title=models.CharField(max_length=50,verbose_name="Başlıq")
    content=RichTextField("Məzmun")
    article_image=models.FileField(blank=True,null=True,verbose_name="Şəkil")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Yaradılma Tarixi") 
    updated_at=models.DateTimeField(auto_now_add=True,verbose_name="Yenilənmə Tarixi")
        #bu asagidaki kod ilk basda menasiz gelirdi lakin indi commentle elaqe yarananda onun foreing key olaraq goturende adi article object kimi yox ele title kimi gelir aydin basa dusmek olur
    def __str__(self):
        return self.title 
    class Meta: # tarixe gore siralama
        ordering = ['-created_at']
class Comment(models.Model): 
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="Məqalə",related_name="comments")
    comment_author=models.CharField(max_length=50,verbose_name="Ad Soyad")
    comment_content=models.CharField(max_length=200,verbose_name="Şərh")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="Yaradılma Tarixi") 
    class Meta:
        ordering = ['-created_at']