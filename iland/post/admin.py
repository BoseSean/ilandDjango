from django.contrib import admin
from .models import Article,Tag,Department
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

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_name',]
    class Meta:
        model = Department
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Department,DepartmentAdmin)