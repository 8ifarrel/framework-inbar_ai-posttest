from django.shortcuts import render

def lihat_barang(request):
  return render(request, 'product_catalog/lihat-barang.html')