from django.shortcuts import render, redirect
import uuid
from .models import URL
from django.http import HttpResponse
from serializers.shortener_serializer import URLSerializer
from rest_framework import viewsets
from rest_framework import generics
# Create your views here.

def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == 'POST':
        name = request.POST['name']
        link = request.POST['link']
        uid = str(uuid.uuid4())[:5]
        new_url = URL(name = name, link=link, uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    
def go(request, pk):
    url_details = URL.objects.get(uuid=pk)
    return redirect(url_details.link)   # 'https://' +

class URLViewSet(viewsets.ModelViewSet):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

class CrudOperations(generics.RetrieveUpdateDestroyAPIView):
    queryset = URL.objects.all()
    serializer_class = URLSerializer

