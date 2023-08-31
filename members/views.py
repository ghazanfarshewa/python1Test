from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import blogpost
from .models import product



def main(request):
  mymembers = product.objects.all().values()
  template = loader.get_template('main.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def product_list_view(request):
  mymembers = product.objects.all().values()
  template = loader.get_template('product_list.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def blogposts(request):
  mymembers = blogpost.objects.all().values()
  template = loader.get_template('my_blog_post.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

