# -*- coding: utf-8 -*-
from django.shortcuts import render
from django import template
def home(request):
    return render(request, "static_handler.html")
