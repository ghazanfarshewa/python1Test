from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('products/', views.product_list_view, name='product_list_view'),
    path('myblog/', views.blogposts, name='blogpost'),
]