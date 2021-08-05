from django.urls import path

from shop import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:pk>/", views.Item_detail, name="Item_detail"),
]
''''
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
'''