from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm                       #oldugumuz forms fylindan RegisterForm imort et
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout     #authenticate istifadeci varsa
from django.contrib import messages


# Create your views here.


def register(request):

    if request.method == "POST":
        form = RegisterForm(request.POST)
        
        if form.is_valid():                                #form.is_valid() clean funksiyasini isledir. True ve ya false qiymeti alir  
            username = form.cleaned_data.get("username")   #formda username icine yazilani goturur
            password = form.cleaned_data.get("password")
            #DB.e yaziriq
            newUser = User(username = username )
            newUser.set_password(password)                 #set_password parolmuzu sifreleyir
            newUser.save()

            login(request,newUser)                         #Login sayesinde db.e qeydiyyatdan sonra avtomatik sisteme daxil olacaq
            messages.success(request, "Qeydiyyatiniz ugurlu oldu")
            return redirect("index")
          
        return render(request, "register.html", {"form": form})
    
    else:
        form = RegisterForm()
        context = {
        "form": form}
    
        return render(request, "register.html", context)
        
        
######################## LOGIN   #############################
def loginUser(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        context = {
            "form":form
                  } 

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username = username, password = password)          #isdifadeci adi ve parolu yoxlanir. True ve ya False qiymetleri alir

            if user is None:                                                       #istifadeci adi ve parolu duz deyilse
                messages.info(request,"İstifadəçi adı və ya parol səhvdir!")        #danger mesajidir eslinde
                return render(request,"login.html", context)
            #eger user true qaytarasa if-e baxmir
            messages.success(request,"Bloga Giriş Etdiniz!")
            login(request, user)
            return redirect("index")
            
          
        return render(request,"login.html",context)
    
    else:                #Get request edilmisse
        form = LoginForm()     
        context = {
            "form":form
                  }  
        return render(request,"login.html",context)                                              

def logoutUser(request):
    logout(request)
    messages.success(request,"Hesabınızdan çıxdınız!")
    return redirect("index")

    