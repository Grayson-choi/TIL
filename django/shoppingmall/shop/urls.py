from django.urls import path
from . import views

app_name = "shop"

urlpatterns = [
    path('<int:id>/<product_slug>/', views.product_detail, name="product_detail"),
    path('', views.product_in_category, name='product_all'),
    path('<slug:category_slug>/', views.product_in_category, name='product_in_categry'),

]
