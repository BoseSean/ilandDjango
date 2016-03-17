from django.contrib import admin
from .models import Article,Tag
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','timestamp']
    search_fields = ['title','body']
    class Meta:
        model = Article

class TagAdmin(admin.ModelAdmin):
    list_display = ['tag_name',]
    class Meta:
        model = Tag

admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag,TagAdmin)