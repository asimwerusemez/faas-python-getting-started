from django.contrib import admin
from django.urls import path
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from accounts.views import LoginView, register
from shop.views import OrderDetailView, OrderListView, ProductDetailView, ProductListView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/', LoginView.as_view(), name='token_obtain_pair'),
    path('auth/register/', register),

    path('orders/', OrderListView.as_view()),
    path('orders/<int:pk>/', OrderDetailView.as_view()),

    path('products/', ProductListView.as_view()),
    path('products/<int:pk>/', ProductDetailView.as_view()),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



