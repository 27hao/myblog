#coding:utf-8
from django.contrib import admin
from blog.models import *
# Register your models here.
class KindAdmin(admin.ModelAdmin):
	list_display=("id","name")
	search_fields=("name",)
	list_filter=('id',)
admin.site.register(Kind,KindAdmin)
class ArticleAdmin(admin.ModelAdmin):
	list_display=("id","title","time","kind")
	search_fields=("title","kind")
	date_hierarchy = 'time'
	list_filter=('id','kind','time')
admin.site.register(Article,ArticleAdmin)
class CommentAdmin(admin.ModelAdmin):
	list_display=("id",'article',"time","email")
	search_fields=("article","email")
	date_hierarchy = 'time'
	list_filter=('id','article','time')
admin.site.register(Comment,CommentAdmin)