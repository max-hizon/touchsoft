from django.urls import path
from . import views
app_name = "orders_page"
urlpatterns = [
    path('', views.orders, name='orders'),
    path("<int:order_id>/details/", views.detail, name="detail"),
    path('add/', views.NewOrder.as_view(), name="new_order")
]