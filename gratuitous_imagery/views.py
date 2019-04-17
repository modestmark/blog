from django.shortcuts import render
from django.http import HttpResponse


def all_albums(request):
  return render(request,'albums/all.html')

# Create your views here.
