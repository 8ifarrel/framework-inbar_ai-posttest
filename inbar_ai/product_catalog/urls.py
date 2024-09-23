from django.urls import path
from . import views

urlpatterns = [
  path("lihat-barang", views.lihat_barang, name="lihat_barang"),
]
