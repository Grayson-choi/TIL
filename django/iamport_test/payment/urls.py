from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail', views.detail, name='detail'),
    path('payment', views.payment, name='payment'),
]