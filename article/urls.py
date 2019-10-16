from django.contrib import admin
from django.urls import path

import article.views
app_name="article" # istediyimiz ad ola biler

from article import views
urlpatterns = [
    
  
    path('', views.articles,name="articles"),
    path('dashboard',views.dashboard,name="dashboard"),
    path('comment/<int:id>',views.addComment,name="comment"),
    path('article/<int:id>', views.articledetail,name="articledetail"),
    path('addArticle',views.addArticle,name="addArticle"),
    path('delete/<int:id>', views.deleteArticle,name="deleteArticle"),
    path('update/<int:id>', views.updateArticle,name="updateArticle"),
    
]

