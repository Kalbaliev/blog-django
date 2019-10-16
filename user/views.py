from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import RegisterForm,LoginForm
from django.contrib import messages
# Create your views here.
def registerUser(request):
  
    form=RegisterForm(request.POST or None) #method yoxlanma sertine daha ehtiyac yoxdu bu sayede
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        newUser=User(username=username)
        newUser.set_password(password)
        newUser.save()
        login(request,newUser)
        messages.success(request,"Qeydiyyat uğurla tamamlandı!")
        return redirect("index")
    context={

        "form":form
    }
    return render(request,"register.html",context)

def loginUser(request):
    form=LoginForm(request.POST or None)

    context={
        "form":form
    }
    if form.is_valid():
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(username=username,password=password) #bazada istifadecini yoxlayir
 
        if user is None:
            messages.info(request,"İstifadəçi adı və ya şifrə xətalı!")
            return render(request,"login.html",context)

        messages.success(request,"Uğurla giriş etdiniz!")
        login(request,user)
        return redirect("index")
    return render(request,"login.html",context)



def logoutUser(request):
    logout(request)
    messages.success(request,"Uğurla çıxış etdiniz!")
    return redirect("index")
