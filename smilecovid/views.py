from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'index.html')

def nhapTrieuChung(request):
    return render(request, 'trieuchung.html')
