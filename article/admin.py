from django.contrib import admin
from .models import Article,Comment
# Register your models here.
# admin.site.register(Article)  bu methodun evezine asagidaki decorator sistemi isleyir

admin.site.register(Comment)

@admin.register(Article)
class AdminArticle(admin.ModelAdmin):

    #ozellikler 

    list_display=["title","author","created_at"] # hansi sutunlar gorsensin
    list_display_links=["title","created_at"] # link elavesi meqaleni acmaq ucun
    search_fields=["title"] # axtaris sutune gore
    list_filter=["created_at"]#filterizasiya sutuna gore
    class Meta: # standart yazilis Article ile AdminArticle -i  elaqelendirir
        model=Article
