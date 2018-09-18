from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  return render(request,'read/index.html')

def article_sql(request):
  return render(request,'articles/WIP_article_sql.html')

def article_nat(request):
  return render(request,'articles/WIP_article_nat.html')
# Create your views here.
