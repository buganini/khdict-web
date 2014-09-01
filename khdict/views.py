from django.http import HttpResponse
from django.shortcuts import render, redirect
import json

def query(request, key):
    d=json.loads(open('/home/buganini/www/khdict/khdict.json').read())
    return HttpResponse(json.dumps(d.get(key, {})), mimetype="application/json")

def index(request):
    return render(request, "khdict/index.html")

