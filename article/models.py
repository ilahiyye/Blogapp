from django.db import models
from ckeditor.fields import RichTextField     #https://github.com/django-ckeditor/django-ckeditor#usage 

# Create your models here.
class Article(models.Model): #Article clasi models.Model miras alir
    author  = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = "Müəllif")  
    title   = models.CharField(max_length=60, verbose_name = "Başlıq") 
    content = RichTextField(verbose_name = "Mövzu")
    created_date  = models.DateTimeField(auto_now_add=True, verbose_name = "Yaradılma tarixi")
    article_image = models.FileField (blank = True, null= True, verbose_name = "Şəkil yüklə")  # Burada blank = True, null= True, o demekdir ki bu sahenin ici dolu da ola biler, bos da
    
    def __str__(self):      #__str__ metodu vasitesi ile yazimiz article evezine title ile gorsenecek
        return self.title      
    class Meta:
        ordering = ["-created_date"] #-created_date vasitesi ile en son yuklenen meqale en birinci gorsenecek

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete = models.CASCADE, verbose_name = "Meqale", related_name="comments") #articli modele(comment modeline)baglamaga calisdigimiz ucun Artikl formunu xarici acar kimi gotururuk
    comment_author  = models.CharField(max_length=30, verbose_name="Ad")                                                                        #related_name="comments" --> article.comments deyerek hemin meqalenin comment cedveli ile elaqe yarada bileceyik
    comment_content = models.CharField(max_length=100,verbose_name="Şərh")
    comment_date    = models.DateTimeField(auto_now_add=True, verbose_name = "Yaradılma tarixi")
    def __str__(self):      #__str__ metodu vasitesi ile yazimiz article evezine title ile gorsenecek
        return self.comment_content       
    class Meta:
        ordering = ["-comment_date"]    #-comment_date vasitesi ile en son yuklenen rey en birinci gorsenecek