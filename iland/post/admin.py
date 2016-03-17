from django.contrib import admin
from .models import Article,Tag
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp']
    search_fields = ['title','body']
    class Meta:
        model = Article

admin.site.register(Article,Tag)
#admin.site.register(ArticleAdmin)