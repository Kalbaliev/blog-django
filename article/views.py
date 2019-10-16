from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .models import Article,Comment

from .forms import ArticleForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):

    # return HttpResponse("Ana Səhifə")
    return render(request,'index.html',{"number":7}) #laraveldeki kimi

def about(request):

    return render(request,'about.html')








def articles(request):

    keyword=request.GET.get("keyword")

    if keyword:
        articles=Article.objects.filter(title__contains=keyword) #like sql emeliyati 
        return render(request,"articles.html",{"articles":articles})
    articles=Article.objects.all()
    return render(request,"articles.html",{"articles":articles})


@login_required(login_url = "user:login")
def dashboard(request):

    articles=Article.objects.filter(author=request.user)
    context={
        "articles":articles
    }
    return render(request,"dashboard.html",context)

def articledetail(request,id):

    # article=Article.objects.filter(id=id).first()
    
    article=get_object_or_404(Article,id=id) # obyekt yoxdursa 404 sehifesi acilir
    
    comments=article.comments.all()

    context={
        "article":article,
        "comments":comments
    }


    return render(request,"articledetail.html",context)






@login_required(login_url = "user:login")
def addArticle(request):
    form=ArticleForm(request.POST or None,request.FILES or None) # sekile gore
    context={
        "form":form
    }
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Məqalə uğurla yaradıldı!")
        return redirect("article:dashboard")
    
    return render(request,"addarticle.html",context)

@login_required(login_url = "user:login")
def updateArticle(request,id):
    article=get_object_or_404(Article,id=id)
    form=ArticleForm(request.POST or None,request.FILES or None,instance=article) # icerisine elave edir
    if form.is_valid():
        article=form.save(commit=False)
        article.author=request.user
        article.save()
        messages.success(request,"Məqalə uğurla yeniləndi!")
        return redirect("article:dashboard")
        
    context={
        "form":form
    }
    return render(request,"update.html",context)

@login_required(login_url = "user:login") # burdaki user urls of userdeki appname nedirse onu yazmaliyiq
def deleteArticle(request,id):
    article=get_object_or_404(Article,id=id)
    article.delete()
    messages.success(request,"Məqalə uğurla silindi")
    return redirect("article:dashboard")


def addComment(request,id):
    article =get_object_or_404(Article,id=id)

    if request.method=='POST':
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        newComment=Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article=article
        newComment.save()

        
    return redirect(reverse("article:articledetail",kwargs={"id":id}))