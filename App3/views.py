from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
def index(request):
     return render(request, "app3.html")