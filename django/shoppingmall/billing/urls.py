from django.urls import path
from . import views
from django.contrib import admin
from billing.views import (
    charge_point,
    PointCheckoutAjaxView,
    PointImpAjaxView,
)


app_name = "billing"

urlpatterns = [

    path('', views.charge_point, name='product_all'),
    path('<slug:category_slug>/', views.PointCheckoutAjaxView, name='point_checkout'),
    path('<int:id>/<product_slug>/', views.PointImpAjaxView, name="point_validation"),

    path('admin/', admin.site.urls),

]
