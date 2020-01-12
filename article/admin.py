from django.contrib import admin
from .models import Article, Comment   #models faylindaki Article import edirik
# Register your models here.
#Article clasina bir decerator yaziriq
admin.site.register(Comment)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display       = ["title","author", "created_date"]
    list_display_links = ["title","author", "created_date"]
    search_fields      = ["title", "author"]
    list_filter        = ["created_date"]

    class Meta: #STANDART
        model = Article   