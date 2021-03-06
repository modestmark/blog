from django.shortcuts import render
from django.http import HttpResponse
from read.models import blogUser, blogPost

def index(request):
  return render(request,'read/index.html')

def article_sql(request):
  return render(request,'articles/article_sql.html')

def article_nat(request):
  return render(request,'articles/article_nat.html')

def article_dns(request):
  return render(request,'articles/article_dns.html')

def contact(request):
  return render(request,'read/contact.html')

def posts(request):
  return render(request,'read/posts.html')

def whereami(request):
  return render(request,'read/whereami.html')
