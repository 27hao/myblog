#coding:utf-8
from django.shortcuts import render_to_response
from blog.models import *
# Create your views here.
i=0;
def index (request,ki,p):
	kinds=Kind.objects.all();
	#articles=Articles.objects.all()
	articles=[{"title":"分享一本不出的Flask Web开发书","time":"2016-11-15","kind":"c/c++"},{"title":"分享一本不出的Flask Web开发书","time":"2016-11-15","kind":"c/c++"},{"title":"分享一本不出的Flask Web开发书","time":"2016-11-15","kind":"c/c++"},{"title":"分享一本不出的Flask Web开发书","time":"2016-11-15","kind":"c/c++"}]
	return render_to_response('index.html',{'kinds':kinds,'title':'网页设计大赛',"articles":articles,"k":ki,"p":p})