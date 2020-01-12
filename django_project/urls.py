"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from article import views                                     #index funksiyasini cagirdiq.  Her bir url ad veririk
from django.conf import settings                              #settings.py metodunu import edirik
from django.conf.urls.static import static                    # content.html funksiyasinin icindeki articles.article_image.url isleye bilmesi ucun bu modul daxil edilir
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name = 'index'),                    #localhost 8000 ("") isledikde index funksiyasi da isleyecek
    path('about/', views.about, name = 'about'),
    path('content/<int:id>', views.content, name='content'),  #dinamic url. article.daki content funksiyasi isleyecek. Yeni db.deki id.ye gore urls gosterir
    path('article/', include('article.urls')) ,               #articlla bagli olan urls-lari articles-in icindeki urls.da axtarib isledecek
    path('user/', include('user.urls')),  
    path('calculator', views.calculator, name='calculator'),  #user.le bagli olan urls-lari userin icindeki urls.da axtarib isledecek
    

    
              ]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)   #Media Url.na ve Root.na catmaq ucun bunu copy edirik
