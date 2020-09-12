from django.contrib import admin
from django.urls import path
from . import views

app_name="products"

urlpatterns = [
    path('update/<int:id>',views.updateProduct,name="updateProduct"),
    path("updateall",views.updateall,name="updateall")

]