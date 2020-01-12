from django.shortcuts import render, redirect, get_object_or_404, reverse
from .form import ArticleForm, BudceForm
from django.contrib import messages
from .models import Article, Comment         #models.py faylinin icindeki Article metodunu cagiririq
from django.contrib.auth.decorators import login_required   # istifadeci girisini yoxlayan hazir dekoratoru import edirik
from django.http import Http404
#from django.contrib.auth import authenticate


# Create your views here.
def about(request):
    return render(request, "about.html")                            #about funksiyasi bu sehife isledikde ise dusecek

def index(request):
    keyword = request.GET.get("keyword")                             #forumda input->icine yazilan keyvordu aliriq
    if keyword:                                                      #eger axtarilis edilibse
        articles=Article.objects.filter(title__contains = keyword)  #title__contains bir DB sorgusudur. Title gore articllari sorgulayiriq. Eger o keyworde beraberdirse articles o olur
        return render(request, "index.html", {"articles": articles})
    articles = Article.objects.all()  
    return render(request,"index.html", {"articles": articles})

#Aile budcesinin planlasdirilmasi
def calculator(request):


    keyword = request.GET.get("budget")

    if keyword:      
        a = int(keyword)
            
        q = a*40//100        #qida
        t = a*5//100         #tehsil
        m = a*5//100         #meiset
        kom = a*15//100      #kommunal
        i = a*4//100         #tehsil
        kir = a*20//100      #kiraye/kredit
        n = a*6//100         #neqliyyat
        kas = a*5//100       #kassa
                

        netice = {
            "Qida":q,
            "Təhsil":t,
            "Müalicə":m,
            "Kommunal":kom,
            "Istirahət":i,
            "Kirayə":kir,
            "Nəqliyyat":n,
            "Kassa":kas,
            } 
        return render(request, "calculator.html", {"netice":netice})
    #else:
        #.info(request,"Zəhmət olmasa aylıq ailə büdcənizi daxil edin!")        #danger mesajidir eslinde
    return render(request,"calculator.html")   

#Meqaleleri db-den alib gostermek
def content(request, id):                                            #dinamic url ucun funksiya
    #articles = Article.objects.filter(id=id).first()                #id-ni ona gore veririk ki dinamik olsun. content.html de id.sine gore meqaleler olsunfilter etdikde liste donur. Ona gore de first() ederek ilk gorduyunu gotursun deyirik
    articles = get_object_or_404(Article, id = id)                   #get_object_or_404 de bize id=id olan Article obyektini cekmeye imkan verir. Eger id yoxdursa onda 404 not found yazilir
    #Reyleri db-den alib meqalelerin altinda goster
    comments = articles.comments.all()                                #articlin commentlerine xarici acar vasitesi ile article.comments deyerek ala bilerik.Cunki models.py de forignkey.e related_name="comments" vermisik
    













    return render(request, "content.html", {"articles" :articles, "comments" :comments})   #tamplate_name = articlin altindaki index.html


@login_required(login_url="/user/login/")                            #eger istifadeci giris etmeyibse onu "/user/login/" url.ne yeni daxil ol sehifesine yonlendirir 
def dashboard(request):
    articles = Article.objects.filter(author = request.user)         #models.py Article import edirik ve butun melumatlari articles deyisenine otururuk
    return render(request, "dashboard.html", {"articles" :articles})

#sehifeye meqale elave etmek
@login_required(login_url="/user/login/")                            #eger istifadeci giris etmeyibse onu "/user/login/" url.ne yeni daxil ol sehifesine yonlendirir
def addArticle(request):
                     
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)                          #POST request olduqda, request.FILES sekilleri yuklemek ucundu
       
        if form.is_valid():
            article = form.save(commit = False)   #formdan articlin content ve title hisselerini goturur ve avtomatik save edir  lakin  bu zaman author olmadigina gore xeta bas verir. form.save(commit=False)etmekle article objesini gotururuk? ancaq save etmeye qoyuruq
            article.author = request.user       #article.author olaraq giris eden sexs olur(request.user)
            article.save()
            messages.success(request, "Məqaləniz uğurla yükləndi!")
            return redirect("index")
        
        return render(request, "addArticle.html", {"form": form})
   
    else:
        form = ArticleForm()                     #GET request olduqda ArticleForm sehifemizde gorsensin
        return render(request, "addArticle.html", {"form": form})

#Meqalelerde deyisiklik etmek)
@login_required(login_url="/user/login/")                            #eger istifadeci giris etmeyibse onu "/user/login/" url.ne yeni daxil ol sehifesine yonlendirir
def updateArticle(request, id):
    articles = get_object_or_404(Article, id = id) #evvel id/ye uygun articlin olub-olmadigini yoxlayir ve form icindeki melumatlari  articles sozluyune menimsedir 

    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance = articles)
        if form.is_valid():
            article = form.save(commit = False)   #form.save(commit=False)etmekle article objesini gotururuk, ancaq save etmeye qoymuruq
            article.author = request.user         #article.author olaraq giris eden sexs olur(request.user)
            article.save()
            messages.success(request, "Dəyişikliklər yadda saxlandı!")
            return redirect("index")
        
        return render(request, "update.html", {"form": form})
   
    else:
        form = ArticleForm(instance = articles)    #instance = articles yazmaqla forummuzun icinde kohne yazilar gorsenir
        return render(request, "update.html", {"form": form})

#Meqaleleri silmek
@login_required(login_url="/user/login/")                            #eger istifadeci giris etmeyibse onu "/user/login/" url.ne yeni daxil ol sehifesine yonlendirir
def deleteArticle(request, id):
    articles = get_object_or_404(Article, id = id)

    articles.delete()   #db-den articl silen funksiya

    messages.success(request, "Məqalə silindi!")

    return redirect("index")  #yeni article/dashboard sehifesine qayitsin

#Meqaleye Rey forumunu elave etmek ve reyleri db yazdirmaq
def addComment(request, id):
    articles = get_object_or_404(Article, id=id)
    if request.method=="POST":
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")

        newComment = Comment(comment_author = comment_author, comment_content = comment_content)  #Yeni commentimizi yaratdiq. daxil edilen melumatlara esasen
        newComment.article = articles
        newComment.save()
        comments = newComment.all()
        return render(request, "content.html", {"Comments":comments})
        
    return redirect(reverse("content", kwargs={"id":id}))
   