from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
	template = loader.get_template('posts/index.html')
	return HttpResponse(template.render({},request))

def detail(request, post_id):
	template = loader.get_template('posts/detail.html')
	return HttpResponse(template.render({'post_id': post_id},request))