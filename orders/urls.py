
from django.urls import path
from . import views
from orders.views import order

urlpatterns = [
    path('', views.order, name='order'),
    path('<int:order_id>/', order, name='order'),
    path('payment/success/', views.payment_success, name='paymentsuccess')
]
