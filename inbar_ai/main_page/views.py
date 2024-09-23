from django.shortcuts import render

def beranda(request):
  return render(request, 'main_page/beranda.html')
