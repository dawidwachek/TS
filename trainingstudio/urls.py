from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    path('accounts/',include('accounts.urls')),
    path('orders/',include('orders.urls')),
]

admin.site.site_header = "Training administration"
admin.site.index_title = "You can change what you can"
admin.site.site_title = "Custom Training"
