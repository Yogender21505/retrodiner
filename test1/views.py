# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
	return  render(request,"index.html")
	
def blog(request):
	return  render(request,"blog.html")

def about(request):
	return  render(request,"about.html")

def burger(request):
	return  render(request,"burger.html")

def hotdog(request):
	return  render(request,"hotdog.html")

def shake(request):
	return  render(request,"shake.html")

def breakfast(request):
	return  render(request,"breakfast.html")

def contact(request):
	return  render(request,"contact.html")